from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import UserLoginForm

def index(request):
    """ Return the index.html file"""

    return render(request, 'index.html')

def logout(request):
    """ Log the user out """

    auth.logout(request)
    messages.success(request, "You have been logged out.")
    return redirect(reverse('index'))


def login(request):
    """ Show a login page to the user """
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username = request.POST['username'],
                                     password = request.POST['password'])
            
            

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You are now logged in.")
            else:
                messages.success(request, "Incorrect login details")

    else:
        login_form = UserLoginForm()


    return render(request, 'login.html', {'login_form':login_form})

