from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_products, name='products'),
    path('upcoming/', views.upcoming_products, name='upcoming'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('upcoming/<int:product_id>/', views.upcoming_product_detail, name='upcoming_product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
