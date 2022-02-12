from django import forms

class UserdateForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        self.login_user = user
        super().__init__(*args, **kwargs)

    height = forms.FloatField(label = '身長')
    weight = forms.FloatField(label = '体重')


