from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# User registration form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ['username', 'full_name', 'email', 'password1', 'password2']

# Contact form
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
