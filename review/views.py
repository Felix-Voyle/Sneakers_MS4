from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product
from .models import Review

from .forms import ReviewForm


def update_product_rating(product):
    """updates products rating"""
    ratings = Review.objects.filter(product=product).values_list('rating', flat=True)
    quantity = len(ratings)
    total = sum(ratings)
    if total > 0:
        average_rating = round(total / quantity, 2)
        product.rating = average_rating
        product.save()
    else:
        product.rating = None
        product.save()


@login_required
def add_review(request, product_id):
    """Allows user to comment on upcoming product"""
    if not request.user:
        messages.error(request, "Sorry you need to sign in to do that")
        return redirect(reverse("home"))

    template = 'reviews/review.html'
    product = get_object_or_404(Product, pk=product_id)
    reviewed_already = Review.objects.filter(user=request.user, product=product)
    data = {'product': product, 'user': request.user, }
    form = ReviewForm(initial=data, instance=product)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if reviewed_already:
            messages.error(request, 'You have already Reviewed this product!'
                           'You can edit your existing review')
            return redirect(reverse(
                'product_detail', args=[product.id]))
        if form.is_valid():
            form.save()
            update_product_rating(product)
            messages.success(request, 'successfully added review')
            return redirect(reverse(
                'product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add review, Please ensure form\
                 is valid.')

    context = {
        'product': product,
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_review(request, review_id):
    """Add a product to the store"""
    if not request.user:
        messages.error(request, "Sorry you need to sign in to do that")
        return redirect(reverse("home"))

    review = get_object_or_404(Review, id=review_id)
    product = get_object_or_404(Product, name=review.product)
    data = {'product': product, 'user': request.user, 'rating': review.rating,
            'review': review}
    form = ReviewForm(initial=data)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            update_product_rating(product)
            messages.success(request, 'successfully edited review')
            return redirect(reverse(
                'product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to edit comment, Please ensure form\
                 is valid.')

    template = 'reviews/edit_review.html'
    context = {
        'review': review,
        'product': product,
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """Delete a product from the store"""
    if not request.user:
        messages.error(request, "Sorry you need to sign in to do that")
        return redirect(reverse("home"))

    review = get_object_or_404(Review, id=review_id)
    product = get_object_or_404(Product, name=review.product)

    review.delete()
    update_product_rating(product)
    messages.success(request, 'Review deleted')
    return redirect(reverse('product_detail', args=[product.id]))
