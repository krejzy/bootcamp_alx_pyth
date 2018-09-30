from django.contrib import admin
from cars.models import Product

class CarsAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'description', 'year of production','mark', 'type of body']
    search_fields = ['name' 'description']

admin.site.register(Cars, CarsAdmin)

# Register your models here.

