from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product

from .forms import CommentForm

@login_required
def comment(request, product_id):
    """Allows user to comment on upcoming product"""
    template = 'comments/comment.html'
    product = get_object_or_404(Product, pk=product_id)
    data = {'product': product, 'user': request.user, }
    form = CommentForm(initial=data, instance=product)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'successfully added comment')
            return redirect(reverse('upcoming_product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add comment, Please ensure form\
                 is valid.')

    context = {
        'product': product,
        'form': form,
    }

    return render(request, template, context)
