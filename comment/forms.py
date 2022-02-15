from django import forms
from django.forms import Textarea, HiddenInput
from .models import Comment



class CommentForm(forms.ModelForm):
    """Comment Form"""
    class Meta:
        """Comment Fields"""
        model = Comment
        fields = ('product', 'user', 'comment',)
        widgets = {
            'product': HiddenInput(),
            'user': HiddenInput(),
            'comment': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
