from django.shortcuts import render, get_object_or_404
from .models import Product, Brand

# Create your views here.


def all_products(request):
    """A view to show products that have released and available to buy"""

    products = Product.objects.all()
    brands = Brand.objects.all()

    context = {
        'products': products,
        'brands': brands,
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
