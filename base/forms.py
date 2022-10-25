from dataclasses import field, fields
from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
class MyUserCreationForm(UserCreationForm):
    name = forms.CharField(label=_('Primeiro nome'))
    surname = forms.CharField(label=_('Ultimo nome'))

    username = forms.CharField(label=_('Username'))
    email = forms.CharField(label=_('Email'))
    password1 = forms.CharField(label=_('Senha'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Confirmar senha'), widget=forms.PasswordInput)
    #message = forms.Charfield(label='Mensagem/Dúvidas', widget=forms.Textarea)
    class Meta:
        model = User
        fields = ['name','surname', 'username', 'email', 'password1', 'password2',]

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants',]


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar','name','surname','username', 'email','bio',]
