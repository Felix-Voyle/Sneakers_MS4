from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product
from .models import Comment

from .forms import CommentForm

@login_required
def add_comment(request, product_id):
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

@login_required
def edit(request, comment_id):
    """Add a product to the store"""
    comment = get_object_or_404(Comment, id=comment_id)
    product = get_object_or_404(Product, name=comment.product)
    data = {'product': product, 'user': request.user, 'comment': comment}
    form = CommentForm(initial=data)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'successfully edited comment')
            return redirect(reverse('upcoming_product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to edit comment, Please ensure form\
                 is valid.')

    template = 'comments/edit_comment.html'
    context = {
        'comment': comment,
        'product': product,
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_comment(request, comment_id):
    """Delete a product from the store"""
    comment = get_object_or_404(Comment, id=comment_id)
    product = get_object_or_404(Product, name=comment.product)
    print('hello')

    comment.delete()
    messages.success(request, 'Comment deleted')
    return redirect(reverse('upcoming_product_detail', args=[product.id]))
