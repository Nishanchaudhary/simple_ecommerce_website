from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')  # Columns in the product list view
    list_editable = ('price',)                       # Make the price field editable in the list view
    search_fields = ('name',)                        # Add a search bar for product names
    list_filter = ('price',)                         # Add filtering options for prices
    list_editable = ('description',)              # Make description read-only
