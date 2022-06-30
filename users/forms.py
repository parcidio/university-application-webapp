from dataclasses import fields
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'email', 'password1',
            'password2'
        ]

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'placeholder': 'Username'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'placeholder': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class':
            'form-control form-control-lg',
            'placeholder':
            'Confirm Password'
        })

        self.fields['email'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'placeholder': 'Email'
        })

        self.fields['first_name'].widget.attrs.update({
            'class':
            'form-control form-control-lg',
            'placeholder':
            'first name'
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'placeholder': 'last name'
        })


class UserUpdateForm(ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'placeholder': 'Email'
        })

        self.fields['first_name'].widget.attrs.update({
            'class':
            'form-control form-control-lg',
            'placeholder':
            'First name'
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'placeholder': 'Last name'
        })


class ProfileUpdateForm(ModelForm):

    class Meta:
        model = Profile
        fields = ['profile_picture']
