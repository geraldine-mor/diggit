from django import forms
from django.core.exceptions import ValidationError
from allauth.account.forms import SignupForm as AllauthSignupForm
from cloudinary.forms import CloudinaryFileField
from .models import Post, Comment, Category


class SignupForm(AllauthSignupForm):
    """
    Customisation of allauth signup form to include first and
    last names and terms of use fields.
    """
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            "placeholder": "First Name"
        })
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            "placeholder": "Last Name"
        })
    )
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            "placeholder": "Username"
        })
    )
    accept_terms = forms.BooleanField(
        required=True,
        label='I have read and accept the Diggit community guidelines',
        label_suffix="",
        widget=forms.CheckboxInput(attrs={
            "class": "form-check-input", "role": "switch"})
    )

    def clean_username(self):
        """Prevent users entering email as username"""
        username = self.cleaned_data['username']
        if '@' in username:
            raise ValidationError(
                "Please choose a public username,"
                " email addresses are not suitable"
            )
        return username

    def save(self, request):
        """
        Called by allauth to save additional fields to the user model
        """
        user = super().save(request)

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        return user


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
