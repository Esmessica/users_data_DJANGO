from django.shortcuts import render
from user_app.forms import UserForm, UserProfileInfoForm
from . import models
from user_app.models import UserProfileInfo
from django.views.generic import TemplateView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.views.generic import ListView


# Create your views here.


def index(request):
    return render(request, 'user_app/index.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


class SpecialView(TemplateView):
    template_name = 'basic_app/special.html'


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'user_app/registration.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})
    #    those files in commas are from the registered.html, they usually match with variable name sin this file


def user_login(request):

    invalid_info = "Invalid login details, please try again"

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:

                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                invalid_info = "Account not active!"
                return render(request,'user_app/errno.html', context=invalid_info)

        else:
            print(f'Login of {username} has failed due to invalid login details')
            return render(request, 'user_app/errno.html', context=invalid_info)

    else:

        return render(request, 'user_app/login.html')


class UsersDataDetailView(DetailView):
    context_object_name = 'users_detail'
    model = models.UserProfileInfo
    template_name = 'user_app/userprofileinfo_list.html'


def users_data(request):
    # Fetch all instances of UserProfileInfo
    user_profiles = UserProfileInfo.objects.all()

    # Pass the user_profiles to the template for rendering
    return render(request, 'user_app/userprofileinfo_list.html', {'UserProfileInfo': user_profiles})



class UserDeleteView(DeleteView):
    model = models.UserProfileInfo
    success_url = reverse_lazy('user_app:users_data')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.object.user.username  # Pass the username to the template
        return context

    def users_data(request):
        # Fetch all instances of UserProfileInfo
        user_profiles = UserProfileInfo.objects.all()

        # Pass the user_profiles to the template for rendering
        return render(request, 'user_app/userprofileinfo_list.html', {'UserProfileInfo': user_profiles})



# def user(request):
#     user_list = User.objects.order_by('user_id')
#     user_dict = {'users': user_list}
#     return render(request, 'user_app/users.html', context=user_dict)

