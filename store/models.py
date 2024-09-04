# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.db import models
from category.models import Category
from django.urls import reverse

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)  # Changed to TextField for longer descriptions
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Changed to DecimalField for accurate pricing
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    def get_url(self):
        """Returns the URL for the product detail view."""
        return reverse('product_detail', args=[self.category.slug, self.slug])
    
    def __str__(self):
        """String representation of the product."""
        return self.product_name
    