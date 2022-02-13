from django import forms
from .models import Product, Brand


class ProductForm(forms.ModelForm):
    """Product Form"""
    class Meta:
        """generates all product fields"""
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        brands = Brand.objects.all()
        freindly_names = [(b.id, b.get_friendly_name) for b in brands]

        self.fields['brand'].choices = freindly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
