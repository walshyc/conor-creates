from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UserLoginForm(forms.Form):
    """ For to allow users to log in """

    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)


class UserRegisterForm(UserCreationForm):
    """ Form for registering new users """
    password1 = forms.CharField(label="Password", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Password Confirmation", widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email','username', 'password1', 'password2' ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')

        if User.objects.filter(email=email).exclude(username = username):
            raise forms.ValidationError(u'Email address must be unique')

        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        

        if not password1 or not password2:
            raise ValidationError("Please confirm you password")
        if password1 != password2:
            raise ValidationError("Passwords must be the same")

        return password2


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']