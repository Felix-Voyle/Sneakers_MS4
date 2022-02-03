from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_products, name='products'),
    path('upcoming', views.upcoming_products, name='upcoming'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('upcoming/<product_id>', views.upcoming_product_detail, name='upcoming_product_detail'),
]
