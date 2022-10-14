from dataclasses import field, fields
from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
class MyUserCreationForm(UserCreationForm):
    name = forms.CharField(label=_('name'))
    username = forms.CharField(label=_('username'))
    email = forms.CharField(label=_('email'))
    password1 = forms.CharField(label=_('password1'))
    password2 = forms.CharField(label=_('password2'))

    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2',]

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants',]


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar','name','username', 'email','bio',]
