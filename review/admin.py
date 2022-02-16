from django.contrib import admin

from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    """Comment Admin"""
    list_display = (
        'product',
        'user',
        'rating',
        'review',
    )

admin.site.register(Review, ReviewAdmin)
