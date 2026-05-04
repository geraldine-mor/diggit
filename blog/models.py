from django.db import models
from django.db.models import UniqueConstraint, Count
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField
from cloudinary.models import CloudinaryField
from .utils import excerpt_generator
from .choices import STATUS, POST_TYPE, COLOUR_CHOICES


class Category(models.Model):
    """
    Represents a category label that can be applied to posts
    """
    name = models.CharField(max_length=30, unique=True)
    label_colour = models.CharField(
        choices=COLOUR_CHOICES, default="#D9BAAF", unique=True)

    class Meta:
        verbose_name_plural = "categories"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Post(models.Model):
    """
    Represents a blog post created by users

    :model:`Category` (ManyToMany), :model:`User`
    """
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from=['title'])
    featured_image = CloudinaryField('image', null=True, blank=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    post_type = models.IntegerField(choices=POST_TYPE, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    excerpt = models.TextField(default="")
    categories = models.ManyToManyField(
        Category, related_name="posts", blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title}"
    
    def first_comment(self):
         """
         Return the most-liked, top-level comment
         """
         return self.comments.top_level().ordered_by_likes().first()

    def comment_count(self):
        return self.comments.count()

    def save(self, *args, **kwargs):
        """
        Override the save() method to auto-generate the excerpt
        on every save
        """
        self.excerpt = excerpt_generator(self.content)
        super().save(*args, **kwargs)


class CommentQuerySet(models.QuerySet):
    """
    Custom queryset for :model:`Comment`, providing reusable methods
    for ordering by likes and filtering to top-level comments only
    """
    def with_like_count(self):
        return self.annotate(
            like_count=Count('likes')
        )

    def ordered_by_likes(self):
        return self.with_like_count().order_by(
            '-like_count', '-created_on')

    def top_level(self):
        return self.filter(parent=None)
    

class Comment(models.Model):
    """
    Represents a comment on a post, or optionally a reply to a comment

    :model:`Post`, :model:`User`, :model:`Comment` (self-referential)
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="commenter"
    )
    content = models.TextField(max_length=1000)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True,
        blank=True, related_name="replies"
    )
    created_on = models.DateTimeField(auto_now_add=True)

    objects = CommentQuerySet.as_manager()

    def __str__(self):
        return f"{self.content}"


class CommentLike(models.Model):
    """
    Represents a like on a comment by a user

    :model:`Comment`, :model:`User`
    """
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE,
        related_name="likes"
    )
    liked_by = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="liked"
    )

    class Meta:
        constraints = [
            # Prevents a user liking comments more than once
            UniqueConstraint(
                fields=["comment", "liked_by"],
                name="unique_comment_like")
        ]
