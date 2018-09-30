from django.contrib import admin
from products.models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'description']
    search_fields = ['name' 'description']

admin.site.register(Product, ProductAdmin)