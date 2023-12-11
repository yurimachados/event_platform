from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ["username","name", "email", "password1", "password2"]