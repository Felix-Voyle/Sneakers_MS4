from datetime import datetime
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from comment.models import Comment
from review.models import Review
from .models import Product, Brand
from .forms import ProductForm, BrandForm


def shop_products(request):
    """A view to show products that have released and available to buy"""

    now = datetime.now()
    date_today = now.date()
    products = Product.objects.filter(release_date__lte=date_today)
    brands = Brand.objects.all()
    query = None
    search_brand = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'brand' in request.GET:
            search_brand = request.GET['brand']
            products = products.filter(
                release_date__lte=date_today,
                brand__name__contains=search_brand)
            search_brand = Brand.objects.filter(name__in=search_brand)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('products'))
            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'brands': brands,
        'search_term': query,
        'search_brand': search_brand,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view to show product details of individual product"""

    product = get_object_or_404(Product, pk=product_id)
    brands = Brand.objects.all()
    reviews = Review.objects.filter(product=product)
    user = request.user

    sizes = []
    for i in range(1, 13):
        sizes.append(i)

    context = {
        'product': product,
        'brands': brands,
        'sizes': sizes,
        'reviews': reviews,
        'user': user,
    }

    return render(request, 'products/product_detail.html', context)


def upcoming_products(request):
    """A view to show product details of individual product"""

    now = datetime.now()
    date_today = now.date()
    products = Product.objects.filter(
        release_date__gt=date_today).order_by('release_date')
    brands = Brand.objects.all()

    context = {
        'products': products,
        'brands': brands,
    }

    return render(request, 'products/upcoming_products.html', context)


def upcoming_product_detail(request, product_id):
    """A view to show product details of individual product"""

    product = get_object_or_404(Product, pk=product_id)
    brands = Brand.objects.all()
    comments = Comment.objects.filter(product=product)
    user = request.user

    context = {
        'product': product,
        'brands': brands,
        'comments': comments,
        'user': user,
    }

    return render(request, 'products/upcoming_product_detail.html', context)


@login_required
def add_product(request):
    """Add a product to the store"""
    brands = Brand.objects.all()
    if not request.user.is_superuser:
        messages.error(request, "Sorry you don't have permission for that")
        return redirect(reverse("home"))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'successfully added product')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product, Please ensure form\
                 is valid.')

    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
        'brands': brands,
    }

    return render(request, template, context)


@login_required
def add_brand(request):
    """Add a product to the store"""
    brands = Brand.objects.all()
    if not request.user.is_superuser:
        messages.error(request, "Sorry you don't have permission for that")
        return redirect(reverse("home"))

    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            brand = form.save()
            messages.success(request, 'successfully added brand')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add brand, Please ensure form\
                 is valid.')

    form = BrandForm()
    template = 'products/add_brand.html'
    context = {
        'form': form,
        'brands': brands,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """Add a product to the store"""
    brands = Brand.objects.all()
    if not request.user.is_superuser:
        messages.error(request, "Sorry you don't have permission for that")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product, Ensure form \
                 is valid')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
        'brands': brands,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """Delete a product from the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry you don't have permission for that")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted')
    return redirect(reverse('products'))
