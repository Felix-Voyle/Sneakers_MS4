from django.urls import path
from . import views

urlpatterns = [
    path('<int:product_id>/', views.add_comment, name='add_comment'),
    path('edit/<int:comment_id>/', views.edit, name='edit'),
    path('delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
