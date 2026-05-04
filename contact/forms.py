from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    """Form to send message to site admin"""
    class Meta:
        model = Message
        fields = ('name', 'email', 'message')
