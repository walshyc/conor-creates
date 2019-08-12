from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from checkout.forms import PayForm, OrderForm
from django.contrib import messages
from django.utils import timezone
from checkout.models import OrderLineItem
from services.models import Service
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET


@login_required
def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = PayForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():

                product = get_object_or_404(Service, pk=id)
                total += quantity * service.price
                order_line_item = OrderLine_Item(
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
                messages.error(request, "Thanks for your payment. We will be in touch soon!")
                request.session['cart'] = {}

                return redirect(reverse('index'))

            else:
                messages.error(request, "We were unable to process the transcation, please try again.")

        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to process the transcation.")

    else:
        order_form = OrderForm()
        payment_form = PayForm()

    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
        
