from django.db import models
from django.contrib.auth.models import User
from product_shared.models import product
    
class orderItems(models.Model):
    owner= models.ForeignKey(User, related_name='tenant_orders', on_delete=models.CASCADE,blank=True, null=True)
    product= models.ForeignKey(product,related_name='tenant_order_items', on_delete=models.CASCADE, blank=True, null=True)
    quantity= models.IntegerField(default=0, null=True, blank=True)
    date_added= models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total= self.product.price * self.quantity
        return total