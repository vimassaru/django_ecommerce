from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.contrib import messages

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
    def get(self, *args, **kwargs):

        http_refer = self.request.META.get(
            'HTTP_REFERER',
            reverse('product:list')
        )

        id_variation = self.request.GET.get('vid')

        if not id_variation:
            messages.error(
                self.request,
                "Product doesn't exist."
            )
            return redirect(http_refer)

        variation = get_object_or_404(models.Variation, id=id_variation)

        if not self.request.session.get('shop_cart'):
            self.request.session['shop_cart'] = {}
            self.request.session.save()

        shop_cart = self.request.session['shop_cart']

        if id_variation in shop_cart:
            # TODO: Variation exist in cart
            pass
        else:
            # TODO: Variation doesn't exist in cart
            pass

        return HttpResponse(f'{variation.product} {variation.product_name}')


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
