from django.urls import path
from . import views


# app name define for html and stuff
app_name = 'user_app'

urlpatterns = [
    path('', views.user, name='user'),
]