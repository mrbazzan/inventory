from django.shortcuts import render
from .models import Product
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.


class ProductList(generic.ListView):
    model = Product
    ordering = 'id'
    paginate_by = 5
    template_name = 'products/home.html'


class ProductCreate(generic.CreateView):
    model = Product
    template_name = "products/new.html"
    success_url = reverse_lazy('products:home')
    fields = ['name']

