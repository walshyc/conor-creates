from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from services.models import Service
from about.forms import ContactUsForm

# View that renders the about page
def about_page(request):
    services = Service.objects.all() 
    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']

            message = "You have a new message from {0}. It says: {1}".format(sender_name, form.cleaned_data['message'])
            send_mail('New Website Query', message, sender_email, ['conorwalsh0703@gmail.com'])
            
            # returns a message to the user to confirm the email has been sent
            messages.success(request, "Your message has been sent, we will be in touch shortly.")

            return redirect(reverse('about'))
        
    else:
        form = ContactUsForm()

    return render(request, 'about.html', {'form': form, 'services':services})    