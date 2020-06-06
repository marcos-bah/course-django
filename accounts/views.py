from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(req):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count() 
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    return render(req, 'accounts/dashboard.html', {
        'orders': orders, 
        'customers': customers, 
        'total_orders': total_orders, 
        'total_customers': total_customers,
        'delivered': delivered,
        'pending' : pending,
    })

def products(req):
    products = Product.objects.all()
    return render(req, 'accounts/products.html', {'products': products})

def customer(req):
    return render(req, 'accounts/customer.html')


