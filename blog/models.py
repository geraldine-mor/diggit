from django.db import models
from django.db.models import UniqueConstraint, Count
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField
from cloudinary.models import CloudinaryField
from .utils import excerpt_generator

STATUS = ((0, "Draft"), (1, "Published"), (2, "Hidden")) 
POST_TYPE = ((0, "Blog"), (1, "Forum"))   

# Create your models here.
class Post(models.Model):
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

    class Meta:
        ordering = ["-created_on"]


    def __str__(self):
        return f"{self.title}"
    

    def first_comment(self):
         return self.comments.top_level().ordered_by_likes().first()
        
    
    def comment_count(self):
        return self.comments.count()


    def save(self, *args, **kwargs):
        self.excerpt = excerpt_generator(self.content)
        super().save(*args, **kwargs)


class CommentQuerySet(models.QuerySet):
    def with_like_count(self):
        return self.annotate(
            like_count=Count('likes')
        )
    
    def ordered_by_likes(self):
        return self.with_like_count().order_by('-like_count', '-created_on')
    
    def top_level(self):
        return self.filter(parent=None)
    

class Comment(models.Model):
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

    # class Meta:
    #     ordering = ["-created_on"]
        
    def __str__(self):
        return f"{self.content}"
    
    

class CommentLike(models.Model):
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
            UniqueConstraint(
                fields=["comment", "liked_by"], 
                name="unique_comment_like")
        ]


