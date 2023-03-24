from django.views.generic import ListView
from .models import orderItems
class orderListView(ListView):
    model= orderItems
    template_name= 'tenant/index.html'
    context_object_name= 'orders'

