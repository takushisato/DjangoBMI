from dataclasses import field
from django import forms
from .models import Userdate

class UserdateForm(forms.ModelForm):

    class Meta:
        model = Userdate
        fields = ('height', 'weight',)


