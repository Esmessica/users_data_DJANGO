from django.shortcuts import render
from user_app.models import User

# Create your views here.


def index(request):
    return render(request, 'user_app/index.html')


def user(request):
    user_list = User.objects.order_by('user_id')
    user_dict = {'users': user_list}
    return render(request, 'user_app/users.html', context=user_dict)