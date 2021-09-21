from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from .models import *


# Create your views here.
def home(request):

    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
        'orders': orders, 'customers': customers, 'total_customers': total_customers, 'total_orders': total_orders, 'delivered': delivered, 'pending': pending
    }
    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

def customers(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {
        'customer': customer, 'orders': orders, 'order_count': order_count
    }
    return render(request, 'accounts/customers.html', context)

def update_order(request,pk):
    try:
        ord = Order.objects.get(id=pk)
    except Order.DoesNotExist:
        return redirect('home')
    if request.method == 'POST':
        ord.product.name = request.POST['name']
        ord.status = request.POST['status']
        ord.save()

        return redirect('home')

    return render(request,'accounts/update.html',{
        'ord': ord
    })


def delete_order(request,pk):
    Order.objects.filter(id=pk).delete()
    return redirect('home')


def delete_customer(request,pk):
    Customer.objects.filter(id=pk).delete()
    return redirect('home')