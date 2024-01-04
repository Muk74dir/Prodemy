from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
class RegistrationForm(UserCreationForm):
    class Meta:
        model =  User
        fields = ['email','name','AccounType']
