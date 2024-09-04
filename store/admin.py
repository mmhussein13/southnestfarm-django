# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    search_fields = ('product_name', 'category__category_name')  # Enable searching
    list_filter = ('is_available', 'category')  # Enable filtering
    ordering = ('product_name',)  # Control the default ordering

admin.site.register(Product, ProductAdmin)
