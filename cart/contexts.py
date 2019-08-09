
from django.shortcuts import get_object_or_404
from services.models import Service


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    
    total = 0
    service_count = 0
    
    
    for id, quantity in cart.items():
        service = get_object_or_404(Service, pk=id)
        
        total += quantity * service.price
        service_count += quantity
        

        cart_items.append({'id': id, 'quantity': quantity, 'service': service})

    
    
    return {'cart_items': cart_items, 'total': total, 'service_count': service_count}