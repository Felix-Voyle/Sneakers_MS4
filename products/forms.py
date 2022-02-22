from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Brand

class DateInput(forms.DateInput):
    """generates date input field"""
    input_type = 'date'


class ProductForm(forms.ModelForm):
    """Product Form"""
    class Meta:
        """generates product fields"""
        model = Product
        fields = '__all__'
        exclude = ('rating',)
        widgets = {
            'release_date': DateInput(),
        }

    image = forms.ImageField(label='Image', required=False,
     widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['release_date'].required = True
        brands = Brand.objects.all()
        friendly_names = [(b.id, b.get_friendly_name) for b in brands]

        self.fields['brand'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class BrandForm(forms.ModelForm):
    """Brand Form"""
    class Meta:
        """generate all brand fields"""
        model = Brand
        fields = '__all__'
