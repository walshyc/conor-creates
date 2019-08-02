from django import forms

class UserLoginForm(forms.Form):
    """ For to allow users to log in """

    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)