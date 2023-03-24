from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from django.contrib.auth.models import User

class Client(TenantMixin):
    name = models.ForeignKey(User, related_name='tenant_client', on_delete=models.CASCADE, blank=True, null=True)
    is_active= models.BooleanField(default=False, blank=True)


    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True

    auto_drop_schema=True


class Domain(DomainMixin):
    pass