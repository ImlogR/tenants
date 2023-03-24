from django.contrib import admin
from product_shared.models import product

# Register your models here.
@admin.register(product)
class productAdmin(admin.ModelAdmin):
    list_display=[
        'owner',
        'name',
        'price',
        'digital',
    ]
