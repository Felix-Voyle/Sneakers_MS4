from django import forms
from django.forms import Textarea
from .models import Comment


class CommentForm(forms.ModelForm):
    """Comment Form"""
    class Meta:
        """Comment Fields"""
        model = Comment
        fields = ('comment',)
        widgets = {
            'comment': Textarea(attrs={'cols': 80, 'rows': 20}),
        }