# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.db import models
#from django.urls import reverse

# Create your models here.
class Category(models.Model):
    """Model representing a product category."""
    category_name   =   models.CharField(max_length=50, unique=True)
    slug            =   models.SlugField(max_length=100, unique=True)
    description     =   models.TextField( blank=True)
    cat_image       =   models.ImageField(upload_to='photos/categories', blank=True)
    
    class Meta:
        verbose_name            = 'category'
        verbose_name_plural     = 'categories'
        
    #def get_absolute_url(self):
        """Returns the URL to access a particular category."""
    #    return reverse('products_by_category', args=[self.slug])
    
    def __str__(self):
        """String representation of the category."""
        return self.category_name

