from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm, PasswordResetForm
from django.contrib.auth import get_user_model


class UserRegistrationForm(UserCreationForm):
    """
    Form for user registration with extended fields.
    """
    email = forms.EmailField(help_text='A valid email address, please.', required=True)

    class Meta:
        model = get_user_model()
        fields = ['username','email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    """
    Form for user login with customizable widgets.
    """
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}),
        label="Username")

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))


class SetPasswordForm(SetPasswordForm):
    """
    Form for setting a new password with a predefined model.
    """
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']
