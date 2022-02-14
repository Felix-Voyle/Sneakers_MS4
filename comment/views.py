from django.shortcuts import render, get_object_or_404
from products.models import Product

# Create your views here.

def comment(request, product_id):
    """Allows user to comment on upcoming product"""
    template = 'comments/comment.html'
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, template, context)
