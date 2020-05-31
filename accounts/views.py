from django.shortcuts import render
from django.http import HttpResponse

def home(req):
    return HttpResponse('home')

def products(req):
    return HttpResponse('products')

def customer(req):
    return HttpResponse('customer')


