from django.urls import path
from .views import orderListView

urlpatterns= [
    path('', orderListView.as_view(), name='order-list'),
]