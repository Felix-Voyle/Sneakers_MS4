from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """checkout"""
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KEEvlCpvTq3sgPLIq3jcJn7fiRfMqkJQ9GXFK74wrHeyOM9hKQAmEdBfAixFq2S4Q9mr8xz2Q9CIZJzVAKAV9h100v9VcrKWY',
        'client_secret': 'test secret key',
    }

    return render(request, template, context)
