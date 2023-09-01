from django.urls import path
from user_app.views import index, user


urlpatterns = [
    path('', user, name='user')
]