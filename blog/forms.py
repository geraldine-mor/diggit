from django import forms

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    accept_terms = forms.BooleanField(
        required=True, 
        label='I have read and accept the Diggit community guidelines',
        label_suffix="",
        widget=forms.CheckboxInput(attrs={"class": "form-check-input", "role": "switch"})
    )

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()