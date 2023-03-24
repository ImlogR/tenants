from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class product(models.Model):
    owner= models.ForeignKey(User, related_name='shared_products', db_constraint=False, on_delete=models.CASCADE, blank=True, null=True)
    name= models.CharField(max_length=200, null=True)
    price= models.DecimalField(max_digits=17, decimal_places=2, null=True)
    digital= models.BooleanField(default=False, null=False, blank=False)