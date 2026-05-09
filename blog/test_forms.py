from django.test import TestCase
from .forms import PostForm, CommentForm
from .models import Category


class TestPostForm(TestCase):

    def setUp(self):
        self.categories = Category(
            name="Miscellaneous",
            label_colour="#000000"
        )
        self.categories.save()

    def test_post_form_is_valid(self):
        """
        Test that the form is valid when title,
        content and category fields are completed
        """

        post_form = PostForm(
            {'title': 'Post Title',
             'content': 'Post content',
             'categories': [1]}
        )
        self.assertTrue(post_form.is_valid())

    def test_title_validation(self):
        """
        Test that missing title field causes the form to be invalid
        """
        post_form = PostForm(
            {'title': '',
             'content': 'Post content',
             'categories': [1]}
        )
        self.assertFalse(post_form.is_valid())

    def test_content_validation(self):
        """
        Test that missing content field causes the form to be invalid
        """
        post_form = PostForm(
            {'title': 'Post Title',
             'content': '',
             'categories': [1]}
        )
        self.assertFalse(post_form.is_valid())

    def test_category_validation(self):
        """
        Test that missing category field causes the form to be invalid
        """
        post_form = PostForm(
            {'title': 'Post Title',
             'content': 'Post content',
             'categories': []}
        )
        self.assertFalse(post_form.is_valid())


class TestCommentForm(TestCase):

    def test_comment_form_is_validated(self):
        """
        Test that the form is valid when the content field filled
        """
        comment_form = CommentForm(
            {'content': 'Comment content'}
        )
        self.assertTrue(comment_form.is_valid())

    def test_content_validation(self):
        """
        Test that empty content field causes the form to be invalid
        """
        comment_form = CommentForm(
            {'content': ''}
        )
        self.assertFalse(comment_form.is_valid())
