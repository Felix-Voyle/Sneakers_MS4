from django.db import models

from products.models import Product
from django.contrib.auth.models import User

class Comment(models.Model):
    """Order Model"""
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='user')
    comment = models.CharField(max_length=400, null=False, blank=False, )

    def __str__(self):
        return self.name
