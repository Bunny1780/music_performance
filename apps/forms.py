from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import MusicEvent

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={
            'class': 'border rounded-md py-2 px-3 focus:outline-none focus:border-blue-500'
        })
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'border rounded-md py-2 px-3 focus:outline-none focus:border-blue-500'
        })
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'class': 'border rounded-md py-2 px-3 focus:outline-none focus:border-blue-500'
        })
    )
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={
            'class': 'border rounded-md py-2 px-3 focus:outline-none focus:border-blue-500'
        })
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'border rounded-md py-2 px-3 focus:outline-none focus:border-blue-500'
        })
    )

class EditForm(forms.ModelForm):
    title = forms.CharField(
        label="Title",
        widget=forms.TextInput(attrs={
            'class': 'w-full border rounded-md py-2 px-3 focus:outline-none focus:border-blue-500'
        })
    )

    class Meta:
        model = MusicEvent
        fields = ['title']