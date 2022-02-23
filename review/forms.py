from django import forms
from django.forms import Textarea, HiddenInput
from .models import Review



class ReviewForm(forms.ModelForm):
    """Comment Form"""
    class Meta:
        """Comment Fields"""
        model = Review
        fields = ('product', 'user', 'rating', 'review',)
        widgets = {
            'product': HiddenInput(),
            'user': HiddenInput(),
            'rating': HiddenInput(),
            'review': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
