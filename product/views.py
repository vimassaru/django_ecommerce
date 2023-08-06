# from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from . import models


class ProductList(ListView):
    model = models.Product
    template_name = 'product/list.html'
    context_object_name = 'products'
    paginate_by = '5'


class ProductDetail(DetailView):
    model = models.Product
    template_name = 'product/detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'


class AddToCart(View):
    # TODO: Remove this log before production
    def get(self, *args, **kwargs):
        return HttpResponse('Add to Cart')


class RemoveFromCart(View):
    # TODO: Remove this log before production
    def get(self, *args, **kwargs):
        return HttpResponse('Remove From Cart')


class ShopCart(View):
    # TODO: Remove this log before production
    def get(self, *args, **kwargs):
        return HttpResponse('ShopCart')


class Checkout(View):
    # TODO: Remove this log before production
    def get(self, *args, **kwargs):
        return HttpResponse('Checkout')
