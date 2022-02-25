from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from products.models import Brand, Product

# Create your views here.


def view_bag(request):
    """A view to return the index page"""

    brands = Brand.objects.all()

    context = {
        'brands': brands,
    }

    return render(request, 'bag/bag.html', context)


def add_to_bag(request, item_id):
    """Add a quantity of specified product to the bag"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        if size in bag[item_id]['items_by_size'].keys():
            bag[item_id]['items_by_size'][size] += quantity
            messages.success(
                request, f'Updated {product.name} Size: {size} quantity \
                     to {bag[item_id]["items_by_size"][size]}')
        else:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(
                request, f'Added {quantity}x {product.name} Size: {size} \
                     to your bag')
    else:
        bag[item_id] = {'items_by_size': {size: quantity}}
        messages.success(
            request, f'Added {quantity}x {product.name} Size: {size} \
                 to your bag')

    request.session['bag'] = bag

    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust quantity of product to specified ammount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id]['items_by_size'][size] = quantity
        messages.success(
                request, f'Updated {product.name} Size: {size} quantity to \
                     {bag[item_id]["items_by_size"][size]}')
    else:
        del bag[item_id]['items_by_size'][size]
        if not bag[item_id]['items_by_size']:
            bag.pop(item_id)
            messages.success(
                request, f'Removed {product.name} Size: {size} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove item from bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if request.POST:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
                messages.success(
                 request, f'Removed {product.name} Size: {size} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as ex:
        messages.error(request, f'Error removing item: {ex}')
        return HttpResponse(status=500)
