from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegisterForm
from django.conf import settings
from services.models import Service, ServiceImage
import os

def index(request):
    """ Return the index.html file"""
    services = Service.objects.all()
    

    return render(request, 'index.html', {'services':services})
@login_required
def logout(request):
    """ Log the user out """

    auth.logout(request)
    messages.success(request, "You have been logged out.")
    return redirect(reverse('index'))


def login(request):
    """ Show a login page to the user """
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username = request.POST['username'],
                                     password = request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You are now logged in.")

                return redirect(reverse('index'))
            else:
                messages.success(request, "Incorrect login details")

    else:
        login_form = UserLoginForm()


    return render(request, 'login.html', {'login_form':login_form})

def register(request):
    """ Shows the register page """

    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        register_form = UserRegisterForm(request.POST)

        if register_form.is_valid():
            user = register_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password = request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have now registered an account.")
            else:
                messages.error(request, "We couldn't register your account.")

    else: 
        register_form = UserRegisterForm()

    register_form = UserRegisterForm()

    return render(request, 'register.html', {'register_form': register_form})

def user_profile(request):
    """ Displays the logged in Users profile """

    user = User.objects.get(email = request.user.email)

    return render(request, 'profile.html', {'profile': user})

