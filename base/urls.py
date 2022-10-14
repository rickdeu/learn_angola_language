from django.urls import path
from . import views
from django.utils.translation import gettext_lazy as _
urlpatterns = [
    path('', views.home, name='home'),
    path(_('login/'), views.loginPage, name='login'),
    path(_('logout/'), views.logoutUser, name='logout'),
    path(_('register/'), views.registerPage, name='register'),
    path(_('profile/<str:pk>/'), views.userProfile, name='user-profile'),
    path(_('room/<str:pk>/'), views.room, name='room'),
    path(_('create-room/'), views.createRoom, name='create-room'),
    path(_('update-room/<str:pk>/'), views.updateRoom, name='update-room'),
    path(_('delete-room/<str:pk>/'), views.deleteRoom, name='delete-room'),
    path(_('delete-message/<str:pk>/'), views.deleteMessage, name='delete-message'),
    path(_('update-user/'), views.updateUser, name='update-user'),
    path(_('topics/'), views.topicsPage, name='topics'),
    path(_('activity/'), views.activityPage, name='activity'),


]