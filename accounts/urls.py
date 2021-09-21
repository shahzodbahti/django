from django.urls import path
from .views import update_order, delete_order, home, products, customers

urlpatterns = [
    path('',home, name='home'),
    path('products/',products, name='products'),
    path('customers/<int:pk>/',customers, name='customers'),
    path('delete/<int:pk>/',delete_order, name='delete_order'),
    path('delete/<int:pk>/',delete_order, name='delete_customer'),
    path('update/<int:pk>/',update_order, name='update_order'),
]