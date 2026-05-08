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
