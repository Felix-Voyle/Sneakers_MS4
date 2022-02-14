from django.shortcuts import render, get_object_or_404
from products.models import Product

from .forms import CommentForm

# Create your views here.

def comment(request, product_id):
    """Allows user to comment on upcoming product"""
    template = 'comments/comment.html'
    product = get_object_or_404(Product, pk=product_id)
    form = CommentForm()

    context = {
        'product': product,
        'form': form,
    }

    return render(request, template, context)
