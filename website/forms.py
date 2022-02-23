from dataclasses import field
from django import forms
from .models import Userdate
from django.contrib.auth.models import User

class UserdateForm(forms.ModelForm):
    class Meta:
        model = Userdate
        fields = ('height', 'weight')

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=40, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=40, required=True, min_length=6, widget=forms.PasswordInput(),)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')