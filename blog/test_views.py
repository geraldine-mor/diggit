from django.urls import reverse
from django.contrib.auth.models import User
from django.test import TestCase
from .forms import CommentForm, PostForm
from .models import Post, Comment, Category


class TestPostListView(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            first_name="John",
            last_name="Smith",
            email="john@smith.com",
            username="JohnSmith",
            password="JSPassword"
        )
        self.user.save()

        self.post = Post.objects.create(
            author=self.user,
            title="Test post",
            content="Test post content",
            status=1
        )
        self.post.save()

    def test_render_blog_page(self):
        """
        Test that the Digging Deeper blog page renders with posts
        """
        response = self.client.get(reverse('digging_deeper'))

        self.assertEqual(response.status_code, 200)
        self.assertIn(self.post, response.context["object_list"])


class TestForumListView(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            first_name="John",
            last_name="Smith",
            email="john@smith.com",
            username="JohnSmith",
            password="JSPassword"
        )
        self.user.save()

        self.post = Post.objects.create(
            author=self.user,
            title="Test post",
            content="Test post content",
            status=1,
            post_type=1
        )
        self.post.save()

    def test_render_blog_page(self):
        """
        Test that the Diggit forum page renders with posts
        """
        response = self.client.get(reverse('diggit_forum'))

        self.assertEqual(response.status_code, 200)
        self.assertIn(self.post, response.context["page_obj"])

    
class TestHomePageView(TestCase):

    def test_render_home_page(self):
        """
        Test that the homepage returns 200 and correct template
        """
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


class TestReadPostView(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            first_name="John",
            last_name="Smith",
            email="john@smith.com",
            username="JohnSmith",
            password="JSPassword"
        )
        self.user.save()

        self.post = Post.objects.create(
            author=self.user,
            title="Test post",
            content="Test post content",
            status=1
        )
        self.post.save()

    def test_render_read_post(self):
        """
        Test that read_post returns 200 for a valid slug
        """
        slug = "test-post"
        response = self.client.get(reverse('read_post', args=[slug]))

        self.assertEqual(response.status_code, 200)

    def test_404_invalid_slug(self):
        """
        Test that read_post returns 404 for an invalid slug
        """
        slug = "post-test"
        response = self.client.get(reverse('read_post', args=[slug]))

        self.assertEqual(response.status_code, 404)