from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegisterForm, UserUpdateForm
from accounts.models import Profile
from payments.models import SingleOrder, SingleOrderLineItem, SingleOrderUpload
from reviews.models import Review
from django.conf import settings
from services.models import Service, ServiceImage
import os

# renders the homepage 
def index(request):
    
    services = Service.objects.all()
    reviews = Review.objects.order_by('-date')[0:10]

    return render(request, 'index.html', {'services':services, 'reviews': reviews})

# view to allow a logged in user to logout
@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "You have been logged out.")
    return redirect(reverse('index'))

# view that allows an already registered user to login
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

# view that registers a new user
def register(request):
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
                
                return redirect(reverse('index'))
            else:
                messages.error(request, "We couldn't register your account.")

    else: 
        register_form = UserRegisterForm()

    register_form = UserRegisterForm()

    return render(request, 'register.html', {'register_form': register_form})


# view that displays a users profile with all their information
def user_profile(request):
    orders = SingleOrderLineItem.objects.all()
        

    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance = request.user)
    
        if user_update_form.is_valid():
            user_update_form.save()
            messages.success(request, "You have updated your profile!")
            return redirect('profile')
    else:
        user_update_form = UserUpdateForm(instance = request.user)
   
    uploads = SingleOrderUpload.objects.all()
    
    user = User.objects.get(email = request.user.email)

    context = {'user_update_form' : user_update_form, 'orders':orders, 'profile': user, 'uploads': uploads}

    return render(request, 'profile.html', context)

