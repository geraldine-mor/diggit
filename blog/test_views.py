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

        self.categories = Category(
            name="Miscellaneous",
            label_colour="#000000"
        )
        self.categories.save()

    def test_render_blog_page(self):
        """
        Test that the Diggit forum page renders with posts
        """
        response = self.client.get(reverse('diggit_forum'))

        self.assertEqual(response.status_code, 200)
        self.assertIn(self.post, response.context["page_obj"])

    def test_create_post_form_submission(self):
        """
        Test for submitting a valid post form
        """
        self.client.login(username="JohnSmith", password="JSPassword")
        data = {
            'title': 'Test User post',
            'content': 'Test user generated content',
            'categories': [1]
        }
        response = self.client.post(
            reverse('diggit_forum'), data, follow=True)
        self.assertRedirects(
            response,
            '/test-user-post/'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Post created", response.content)

    def test_logged_out_user_cannot_post(self):
        """
        Test that logged out users can't create a post
        """

        data = {
            'title': 'Logged Out Test',
            'content': 'Test user generated content',
            'categories': [1]
        }
        response = self.client.post(reverse('diggit_forum'), data)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            Post.objects.filter(title="Logged Out Test").exists())


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
        response = self.client.get(
            reverse('read_post', args=[self.post.slug]))

        self.assertEqual(response.status_code, 200)

    def test_404_invalid_slug(self):
        """
        Test that read_post returns 404 for an invalid slug
        """
        slug = "post-test"
        response = self.client.get(reverse('read_post', args=[slug]))

        self.assertEqual(response.status_code, 404)

    def test_comment_form_submission(self):
        """
        Test for submitting a valid comment form
        """
        self.client.login(username="JohnSmith", password="JSPassword")
        data = {
            'content': 'Test comment content',
        }
        response = self.client.post(
            reverse('read_post',
                    args=[self.post.slug]), data, follow=True)
        self.assertRedirects(
            response,
            f"/{self.post.slug}/"
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Comment saved", response.content)


class TestEditPostView(TestCase):

    def setUp(self):
        self.user_a = User.objects.create_user(
            first_name="John",
            last_name="Smith",
            email="john@smith.com",
            username="JohnSmith",
            password="JSPassword"
        )
        self.user_a.save()

        self.user_b = User.objects.create_user(
            first_name="Jane",
            last_name="Doe",
            email="jane@doe.com",
            username="JaneDoe",
            password="JDPassword"
        )
        self.user_b.save()

        self.post = Post.objects.create(
            author=self.user_a,
            title="Test post",
            content="Test post content",
            status=1,
            post_type=1
        )
        self.post.save()

        self.categories = Category(
            name="Miscellaneous",
            label_colour="#000000"
        )
        self.categories.save()

    def test_user_can_edit_own_post(self):
        """
        Test that a logged in user can edit their own posts
        """
        self.client.login(username="JohnSmith", password="JSPassword")
        data = {
            "title": "Test Post",
            "content": "Change post content",
            "categories": [1]
        }
        response = self.client.post(reverse(
            'edit_post', args=[self.post.slug]), data, follow=True)
        self.assertRedirects(
            response,
            f"/{self.post.slug}/"
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Post Updated!", response.content)
        self.assertTrue(
            Post.objects.filter(content="Change post content").exists())

    def test_cannot_edit_not_other_users_post(self):
        """
        Test that a logged in user can't edit another user's posts
        """
        self.client.login(username="JaneDoe", password="JDPassword")
        data = {
            "title": "Test Post",
            "content": "Change post content",
            "categories": [1]
        }
        response = self.client.post(reverse(
            'edit_post', args=[self.post.slug]), data, follow=True)
        self.assertRedirects(
            response,
            '/diggit_forum/'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"You can only edit your own posts.", response.content)
        self.assertFalse(
            Post.objects.filter(content="Change post content").exists())


class TestDeletePostView(TestCase):

    def setUp(self):
        self.user_a = User.objects.create_user(
            first_name="John",
            last_name="Smith",
            email="john@smith.com",
            username="JohnSmith",
            password="JSPassword"
        )
        self.user_a.save()

        self.user_b = User.objects.create_user(
            first_name="Jane",
            last_name="Doe",
            email="jane@doe.com",
            username="JaneDoe",
            password="JDPassword"
        )
        self.user_b.save()

        self.post = Post.objects.create(
            author=self.user_a,
            title="Test post",
            content="Test post content",
            status=1,
            post_type=1
        )
        self.post.save()

    def test_user_can_delete_own_post(self):
        """
        Test that logged in users can delete own posts
        """
        self.client.login(username="JohnSmith", password="JSPassword")
        response = self.client.post(reverse(
            'delete_post', args=[self.post.slug]), follow=True)
        self.assertRedirects(
            response,
            '/diggit_forum/'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Post deleted!", response.content)
        self.assertFalse(
            Post.objects.filter(title="Test post").exists())

    def test_user_b_cannot_delete_user_a_post(self):
        """
        Test that logged in users can't delete other user's posts
        """
        self.client.login(username="JaneDoe", password="JDPassword")
        response = self.client.post(reverse(
            'delete_post', args=[self.post.slug]), follow=True)
        self.assertRedirects(
            response,
            '/diggit_forum/'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"You cannot delete this post!", response.content)
        self.assertTrue(
            Post.objects.filter(title="Test post").exists())


class TestEditCommentView(TestCase):

    def setUp(self):
        self.user_a = User.objects.create_user(
            first_name="John",
            last_name="Smith",
            email="john@smith.com",
            username="JohnSmith",
            password="JSPassword"
        )
        self.user_a.save()

        self.user_b = User.objects.create_user(
            first_name="Jane",
            last_name="Doe",
            email="jane@doe.com",
            username="JaneDoe",
            password="JDPassword"
        )
        self.user_b.save()

        self.post = Post.objects.create(
            author=self.user_a,
            title="Test post",
            content="Test post content",
            status=1,
            post_type=1
        )
        self.post.save()

        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user_b,
            content="Test comment"
        )
        self.comment.save()

    def test_user_can_edit_own_comment(self):
        """
        Test that a logged in user can edit their own comments
        """
        self.client.login(username="JaneDoe", password="JDPassword")
        data = {"content": "Change comment content"}
        response = self.client.post(
            reverse('edit_comment', args=[self.post.slug, self.comment.id]),
            data, follow=True)
        self.assertRedirects(
            response,
            f"/{self.post.slug}/"
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Comment Updated!", response.content)
        self.assertTrue(
            Comment.objects.filter(content="Change comment content").exists())

    def test_cannot_edit_not_other_users_comment(self):
        """
        Test that a logged in user can't edit another user's comments
        """
        self.client.login(username="JohnSmith", password="JSPassword")
        data = {"content": "Change comment content"}
        response = self.client.post(reverse(
            'edit_comment', args=[self.post.slug, self.comment.id]),
            data, follow=True)
        self.assertRedirects(
            response,
            f"/{self.post.slug}/"
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"You can only edit your own comments.", response.content)
        self.assertFalse(
            Comment.objects.filter(content="Change comment content").exists())


class TestDeleteCommentView(TestCase):

    def setUp(self):
        self.user_a = User.objects.create_user(
            first_name="John",
            last_name="Smith",
            email="john@smith.com",
            username="JohnSmith",
            password="JSPassword"
        )
        self.user_a.save()

        self.user_b = User.objects.create_user(
            first_name="Jane",
            last_name="Doe",
            email="jane@doe.com",
            username="JaneDoe",
            password="JDPassword"
        )
        self.user_b.save()

        self.post = Post.objects.create(
            author=self.user_a,
            title="Test post",
            content="Test post content",
            status=1,
            post_type=1
        )
        self.post.save()

        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user_b,
            content="Test comment"
        )
        self.comment.save()

    def test_user_can_delete_own_comment(self):
        """
        Test that logged in users can delete own comments
        """
        self.client.login(username="JaneDoe", password="JDPassword")
        response = self.client.post(reverse(
            'delete_comment',
            args=[self.post.slug, self.comment.id]),
            follow=True)
        self.assertRedirects(
            response,
            f"/{self.post.slug}/"
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Comment deleted!", response.content)
        self.assertFalse(
            Comment.objects.filter(content="Test comment").exists())

    def test_user_a_cannot_delete_user_b_comment(self):
        """
        Test that logged in users can't delete other user's comments
        """
        self.client.login(username="JohnSmith", password="JSPassword")
        response = self.client.post(reverse(
            'delete_comment',
            args=[self.post.slug, self.comment.id]), follow=True)
        self.assertRedirects(
            response,
            f"/{self.post.slug}/"
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"You cannot delete this comment!", response.content)
        self.assertTrue(
            Comment.objects.filter(content="Test comment").exists())
