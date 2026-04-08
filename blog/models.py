from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))    

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="posts" 
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=210, unique=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)