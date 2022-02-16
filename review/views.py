from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product
from .models import Review

from .forms import ReviewForm


@login_required
def add_review(request, product_id):
    """Allows user to comment on upcoming product"""
    if not request.user:
        messages.error(request, "Sorry you need to sign in to do that")
        return redirect(reverse("home"))

    template = 'reviews/review.html'
    product = get_object_or_404(Product, pk=product_id)
    reviewed_already = Review.objects.filter(product=product)
    data = {'product': product, 'user': request.user, }
    form = ReviewForm(initial=data, instance=product)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if reviewed_already:
            messages.error(request, 'You have already Reviewed this product! You can edit your existing review')
            return redirect(reverse(
                'product_detail', args=[product.id]))
        if form.is_valid():
            form.save()
            messages.success(request, 'successfully added review')
            return redirect(reverse(
                'product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add comment, Please ensure form\
                 is valid.')

    context = {
        'product': product,
        'form': form,
    }

    return render(request, template, context)
