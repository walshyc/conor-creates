
from django.shortcuts import get_object_or_404
from services.models import Service


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    
    cart_total = 0
    service_count = 0

    
    for id, quantity in cart.items():
        service_count = 0
        service = get_object_or_404(Service, pk=id)
        cart_total += quantity * service.price
        service_count += quantity
        service_total = service_count * service.price 

        brief = request.POST.get('brief')

        cart_items.append({'id': id, 'quantity': quantity, 'service': service, 'service_total': service_total, 'brief': brief})

    
    
    return {'cart_items': cart_items, 'cart_total': cart_total, 'service_count': service_count}