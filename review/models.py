from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from django.contrib.auth.models import User
from products.models import Product


class Review(models.Model):
    """Order Model"""
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='user_review')
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    review = models.CharField(max_length=400, null=False, blank=False)

    def __str__(self):
        return str(self.rating)
