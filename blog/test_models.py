from django.contrib.auth.models import User
from django.test import TestCase
from .models import Post, Comment, Category


class TestCategoryModel(TestCase):

    def setUp(self):
        self.category = Category(
            name="Other",
            label_colour="Beige"
        )
        self.category.save()

    def test_str_method(self):
        """
        Test that the model's __str__() method returns the name
        """
        category_str = "Other"
        self.assertEqual(category_str, str(self.category))


class TestPostModel(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            first_name="John",
            last_name="Smith",
            email="john@smith.com",
            username="JohnSmith",
            password="JSPassword"
        )
        self.user.save()

        self.post = Post(
            author=self.user,
            title="Test post",
            content="Test post content"
        )
        self.post.save()

    def test_str_method(self):
        """
        Test that the model's __str__() method returns the title
        """
        post_str = "Test post"
        self.assertEqual(post_str, str(self.post))


class TestCommentModel(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            first_name="John",
            last_name="Smith",
            email="john@smith.com",
            username="JohnSmith",
            password="JSPassword"
        )
        self.user.save()

        self.post = Post(
            author=self.user,
            title="Test post",
            content="Test post content"
        )
        self.post.save()

        self.comment = Comment(
            post=self.post,
            author=self.user,
            content="Test comment content"
        )
        self.comment.save()

    def test_str_method(self):
        """
        Test that the __str__() method returns the content
        """
        comment_str = "Test comment content"
        self.assertEqual(comment_str, str(self.comment))
