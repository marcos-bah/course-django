from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm

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

    return render(req, 'accounts/products.html', {
        'products': products
    })

def customer(req, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    total_orders = orders.count()

    return render(req, 'accounts/customer.html', {
        'customer': customer,
        'orders': orders,
        'total_orders' : total_orders,
    })

def createOrder(req):
    form = OrderForm()
    if req.method == 'POST':
        #print(req.POST)
        form = OrderForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(req, 'accounts/order_form.html', {
        'form': form
    })

def updateOrder(req, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if req.method == 'POST':
        form = OrderForm(req.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(req, 'accounts/order_form.html', {
        'form': form
    })

def deleteOrder(req, pk):
    order = Order.objects.get(id=pk)
    if req.method == 'POST':
        order.delete()
        return redirect('/')
    return render(req, 'accounts/delete.html', {
        'item': order
    })

