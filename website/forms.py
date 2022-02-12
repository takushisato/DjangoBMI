from django import forms

class UserdateForm(forms.Form):

    height = forms.FloatField(label = '身長')
    weight = forms.FloatField(label = '体重')


