from django import forms
from cloudinary.forms import CloudinaryFileField
from .models import Post, Comment, Category


class SignupForm(forms.Form):
    """
    Customisation of allauth signup form to include first and
    last names and terms of use fields.
    """
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    accept_terms = forms.BooleanField(
        required=True,
        label='I have read and accept the Diggit community guidelines',
        label_suffix="",
        widget=forms.CheckboxInput(attrs={
            "class": "form-check-input", "role": "switch"})
    )

    def signup(self, request, user):
        """
        Called by allauth to save additional fields to the user model
        """
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()


class CommentForm(forms.ModelForm):
    """Form to add/edit a comment on a post"""
    class Meta:
        model = Comment
        fields = ('content',)


class PostForm(forms.ModelForm):
    """
    Post creation/edit form includes Cloudinary field for image upload
    handling and categories many to many field
    """
    featured_image = CloudinaryFileField(required=False)
    categories = forms.ModelMultipleChoiceField(
        Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

    class Meta:
        model = Post
        fields = ('title', 'content', 'featured_image', 'categories')
