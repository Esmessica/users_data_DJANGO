from django.urls import path
from . import views


# app name define for html and stuff
app_name = 'user_app'

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name='login'),
    path('user_login/', views.user_login, name='user_login'),
    path('users/', views.users_data, name='users_data'),
    path('delete/<int:pk>', views.UserDeleteView.as_view(), name="delete"),

]