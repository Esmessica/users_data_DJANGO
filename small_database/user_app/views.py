from django.shortcuts import render
from user_app.forms import UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout


# Create your views here.


def index(request):
    return render(request, 'user_app/index.html')


def user(request):
    user_list = User.objects.order_by('user_id')
    user_dict = {'users': user_list}
    return render(request, 'user_app/users.html', context=user_dict)

