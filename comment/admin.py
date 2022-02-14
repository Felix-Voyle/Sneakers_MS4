from django.contrib import admin

from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    """Comment Admin"""
    list_display = (
        'product',
        'user',
        'comment',
    )

admin.site.register(Comment, CommentAdmin)
