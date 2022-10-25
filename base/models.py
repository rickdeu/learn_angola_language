from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    name = models.CharField(_('name'),max_length=200, null=True)
    surname = models.CharField(_('surname'),max_length=200, null=True)

    email = models.EmailField(_('email'),unique=True)
    bio = models.TextField(_('bio'),null=True, blank=True)
    avatar = models.ImageField(_('avatar'),null=True, default='avatar.svg')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
class Topic(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
class Room(models.Model):
    host = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    ) 
    topic = models.ForeignKey(
        Topic,
        on_delete=models.SET_NULL,
        null=True
    ) 
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants =  models.ManyToManyField(
        User, 
        related_name='participants',
        blank=True
        )
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name
class Message(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete = models.CASCADE
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE
    )
    body = models.TextField()
    img = models.ImageField(_('imagem'),null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]


class Suport(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(_('logo'),null=True, default='avatar.svg')
    links = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name