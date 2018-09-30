from django.contrib import admin

from engine.models import Product

class EngineAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'description', 'engine capacity', 'number of cylinders','combustion cycle']
    search_fields = ['name' 'description']

admin.site.register(Engine, EngineAdmin)

# Register your models here.


