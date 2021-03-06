from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)
    firstname = forms.CharField(max_length=240)
    age = forms.IntegerField()
    homepage = forms.URLField()
