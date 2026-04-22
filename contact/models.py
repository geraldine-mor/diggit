from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ["read", "-created_on"]

    
    def __str__(self):
        return f"{self.message}"
