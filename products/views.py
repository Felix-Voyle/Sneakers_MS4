from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Brand

# Create your views here.


def all_products(request):
    """A view to show products that have released and available to buy"""

    products = Product.objects.all()
    brands = Brand.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'brands': brands,
        'search_term': query
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view to show product details of individual product"""

    product = get_object_or_404(Product, pk=product_id)
    brands = Brand.objects.all()

    context = {
        'product': product,
        'brands': brands,
    }

    return render(request, 'products/product_detail.html', context)
