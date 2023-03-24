from django.contrib import admin
from .models import orderItems

# Register your models here.
@admin.register(orderItems)
class orderItemAdmin(admin.ModelAdmin):
    list_display=[
        'owner',
        'product',
        'quantity',
        'date_added',
        'get_total'
    ]
