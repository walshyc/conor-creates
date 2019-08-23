import random
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, reverse
from payments.forms import SinglePayForm, SingleOrderForm
from payments.models import SingleOrderLineItem, SingleOrder
from services.models import Service, ServiceImage
from reviews.models import Review
from django.contrib import messages
from django.conf import settings
from django.utils import timezone
from django.core.mail import send_mail
import stripe

# API details for Stripe
stripe.api_key = settings.STRIPE_SECRET

# view that displays all the services 
def all_services(request):
    services = Service.objects.all()
    service_images = services.all()

    return render(request, 'services.html', {'services': services, 'images': service_images})

# view that displays a single service and process the payment
def single_service(request, pk):
    service = get_object_or_404(Service, pk=pk)
    service_images = service.images.all()
    reviews = Review.objects.order_by('-pk')[:40]


    if request.method == "POST":
        order_form = SingleOrderForm(request.POST)
        payment_form = SinglePayForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.user = request.user
            order.save()
            quantity = 1
            serviceID = service.id

            service = get_object_or_404(Service, pk=serviceID)
            total = service.price
            order_line_item = SingleOrderLineItem(
                order=order,
                service=service,
                quantity=quantity
            )

            order_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],

                )
            except stripe.error.CardError:
                messages.error(
                    request, "The payment has not been processed, please try again.")

            if customer.paid:
                customer_email = order_form.cleaned_data['email']
                customer_name = order_form.cleaned_data['name']
                customer_brief = order_form.cleaned_data['brief']

                # sends an email to the customer with their order information
                customer_message = "Thanks for your order for {0}. You have paid €{1}. Check your profile page on https://conor-creates.herokuapp.com/accounts/profile/ to see if your graphic has been uploaded".format(service.name, total)
                send_mail('Your order for {0} on ConorCreates'.format(service.name), customer_message, settings.ADMIN_EMAIL , [customer_email])
                messages.success(request, "Thanks for your payment, your order information is below. Your graphic will be uploaded to this page once complete.")

                # sends an email to the admin with the details of the order
                admin_message = "A new order has been placed on ConorCreates for {0} - €{1}. The customer details are: Name: {2}, Email: {3}, Brief: {4} ".format(service.name, total, customer_name, customer_email, customer_brief)
                send_mail('New Order for {0} on ConorCreates'.format(service.name), admin_message, customer_email , [settings.ADMIN_EMAIL])

                return redirect(reverse('profile'))

            else:
                messages.error(
                    request, "We were unable to process the transcation, please try again.")

        else:
            print(payment_form.errors)
            messages.error(request, "Forms did not validate")

    else:
        order_form = SingleOrderForm()
        payment_form = SinglePayForm()

    return render(request, 'single-service.html', {'service': service, 'images': service_images, 'order_form': order_form, 'payment_form': payment_form, 'reviews': reviews, 'publishable': settings.STRIPE_PUBLISHABLE})
