from django.contrib import admin
from .models import Client, Domain
# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display= ['name', 'schema_name']

@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display=['domain']

# admin.site.register(Domain)