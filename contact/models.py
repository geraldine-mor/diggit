from django.db import models


class Message(models.Model):
    """Represents a message sent to the site admin"""
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ["read", "-created_on"]

    def __str__(self):
        return f"{self.message}"
