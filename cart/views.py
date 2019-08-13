from django.shortcuts import render, reverse, redirect

def view_cart(request):
    """ Shows the content of the carts """

    return render(request, 'cart.html')


    
def add_to_cart(request, id):
    
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if id in cart:
        cart[id] = int(cart[id]) + quantity   

    else:
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart

    return render(request, 'cart.html')

def adjust_cart(request, id):

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:

        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    
    return redirect(reverse('view_cart'))