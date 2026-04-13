from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField
from .utils import excerpt_generator

STATUS = ((0, "Draft"), (1, "Published"))    

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="posts" 
    )
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from=['title'])
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    excerpt = models.TextField(default="")

    class Meta:
        ordering = ["-created_on"]


    def __str__(self):
        return f"{self.title}"
    

    def save(self, *args, **kwargs):
        self.excerpt = excerpt_generator(self.content)
        super().save(*args, **kwargs)
