import random
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, reverse
from payments.forms import SinglePayForm, SingleOrderForm
from payments.models import SingleOrderLineItem, SingleOrder
from .models import Service, ServiceImage
from django.contrib import messages
from django.conf import settings
from django.utils import timezone
import stripe

stripe.api_key = settings.STRIPE_SECRET

def all_services(request):
    services = Service.objects.all()
    service_images = services.all()

    return render(request, 'services.html', {'services': services, 'images': service_images})


def single_service(request, pk):
    service = get_object_or_404(Service, pk=pk)
    service_images = service.images.all()

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
                messages.success(request, "Thanks for your payment, your order information is below. Your graphic will be uploaded to this page once complete.")

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

    return render(request, 'single-service.html', {'service': service, 'images': service_images, 'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
