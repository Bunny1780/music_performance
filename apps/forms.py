from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import MusicEvent

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class EditForm(forms.ModelForm):
    class Meta:
        model = MusicEvent
        fields = ['title']