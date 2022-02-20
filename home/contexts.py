from products.models import Brand

def home_context():
    """gets brands for homepage"""
    
    brands = Brand.objects.all()

    context = {
        'brands': brands,
    }

    return context