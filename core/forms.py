from django import forms
from .models import Event, Company
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ["username","name", "email", "password1", "password2"]

class EventForm(forms.ModelForm):
    companies = Company.objects.filter()

    class Meta:
        model = Event
        fields = ['company','title', 'description', 'image', 'cover', 'location', 'date']
        widgets = {
            'date': forms.DateTimeInput(format=('%Y-%m-%dT%H:%M'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'datetime-local'}),
        }
