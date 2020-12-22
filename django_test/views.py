from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Product
# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = 'django_test/index.html'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'django_test/product_create.html'
    fields = ['name', 'description', 'price']
