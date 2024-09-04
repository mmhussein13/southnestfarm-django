# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.contrib import admin
from .models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')
    ordering = ('category_name',)  # Control the default ordering
    search_fields = ('category_name', 'slug')  # Enable search functionality
    list_filter = ('category_name', 'slug')  # Optional: Add filters if more fields are added
    list_editable = ('slug',)  # Optional: Allow inline editing of slug

admin.site.register(Category, CategoryAdmin)
