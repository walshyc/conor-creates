from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ContactUsForm


def about_page(request):

    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']

            message = "You have a new message from {0}. It says: {1}".format(sender_name, form.cleaned_data['message'])

            send_mail('New Website Query', message, sender_email, ['conorwalsh0703@gmail.com'])


            messages.success(request, "Your message has been sent, we will be in touch shortly.")

            return redirect(reverse('about'))
        
    else:
        form = ContactUsForm()

    return render(request, 'about.html', {'form': form})    