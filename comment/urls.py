from django.urls import path
from . import views

urlpatterns = [
    path('<int:product_id>/', views.comment, name='comment'),
    path('edit/<int:comment_id>/', views.edit, name='edit'),
]
