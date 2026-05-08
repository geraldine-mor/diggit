from django.test import TestCase
from .forms import PostForm, CommentForm


class TestPostForm(TestCase):

    def test_post_form_is_valid(self):
        """
        Test that the form is valid when title,
        content and category fields are completed
        """
        post_form = PostForm(
            {'title': 'Post Title',
             'content': 'Post content',
             'categories': []}
        )
        self.assertTrue(post_form.is_valid(), post_form.errors)
