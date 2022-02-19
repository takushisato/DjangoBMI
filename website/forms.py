from dataclasses import field
from django import forms
from .models import Userdate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class UserdateForm(forms.ModelForm):
    class Meta:
        model = Userdate
        fields = ('height', 'weight',)

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=40, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=40, required=True, min_length=6, widget=forms.PasswordInput(),)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
 
    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError("正しいメールアドレスを指定して下さい。")
    
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        else:
            raise ValidationError("このメールアドレスは既に使用されています。別のメールアドレスを指定してください")
