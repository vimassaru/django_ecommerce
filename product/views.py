# from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views import View


class ProductList(ListView):
    # TODO: Remove this log before production
    def get(self, *args, **kwargs):
        return HttpResponse('Product List')


class ProductDetail(View):
    # TODO: Remove this log before production
    def get(self, *args, **kwargs):
        return HttpResponse('Product Detail')


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
