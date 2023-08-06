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
        # if self.request.session.get('shop_cart'):
        #     del self.request.session['shop_cart']
        #     self.request.session.save()
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
        variation_stock = variation.stock
        product = variation.product

        product_id = product.id
        product_name = product.product_name
        variation_name = variation.product_name or ''
        unit_price = variation.marketing_price
        unit_off_price = variation.marketing_off_price
        amount = 1
        slug = product.slug
        image = product.image

        if image:
            image = image.name
        else:
            image = ''

        if variation.stock < 1:
            messages.error(
                self.request,
                'Product out of stock'
            )
            return redirect(http_refer)

        if not self.request.session.get('shop_cart'):
            self.request.session['shop_cart'] = {}
            self.request.session.save()

        shop_cart = self.request.session['shop_cart']

        if id_variation in shop_cart:
            shop_cart_amount = shop_cart[id_variation]['amount']
            shop_cart_amount += 1

            if variation_stock < shop_cart_amount:
                messages.warning(
                    self.request,
                    f"We're out of stock for {shop_cart_amount}x in"
                    f'product {shop_cart_amount}. We added {variation_stock}x'
                    f'on your shopping cart.'
                )
                shop_cart_amount = variation_stock

            shop_cart[id_variation]['amount'] = shop_cart_amount
            shop_cart[id_variation]['quantitative_price'] = unit_price * \
                shop_cart_amount

            qttve_off_price = unit_off_price * shop_cart_amount
            shop_cart[id_variation]['quantitative_off_price'] = qttve_off_price
        else:
            shop_cart[id_variation] = {
                'product_id': product_id,
                'product_name': product_name,
                'variation_name': variation_name,
                'id_variation': id_variation,
                'unit_price': unit_price,
                'unit_off_price': unit_off_price,
                'quantitative_price': unit_price,
                'quantitative_off_price': unit_off_price,
                'amount': amount,
                'slug': slug,
                'image': image,
            }

        self.request.session.save()

        messages.success(
            self.request,
            f'Successfully added product {product_name} {variation_name}'
            f'to cart {shop_cart[id_variation]["amount"]}x.'
        )
        return redirect(http_refer)


class RemoveFromCart(View):
    # TODO: Remove this log before production
    def get(self, *args, **kwargs):
        http_refer = self.request.META.get(
            'HTTP_REFERER',
            reverse('product:list')
        )

        id_variation = self.request.GET.get('vid')

        if not id_variation:
            return redirect(http_refer)

        if not self.request.session.get('shop_cart'):
            return redirect(http_refer)

        if id_variation not in self.request.session['shop_cart']:
            return redirect(http_refer)

        shop_cart = self.request.session['shop_cart'][id_variation]

        messages.success(
            self.request,
            f'Successfully removed {shop_cart["product_name"]} '
            f'{shop_cart["variation_name"]}'
            f'from your shopping cart.'
        )

        del self.request.session['shop_cart'][id_variation]
        self.request.session.save()
        return redirect(http_refer)


class ShopCart(View):
    def get(self, *args, **kwargs):
        context = {
            'shop_cart': self.request.session.get('shop_cart', {})
        }

        return render(self.request, 'product/shop_cart.html', context)


class Checkout(View):
    # TODO: Remove this log before production
    def get(self, *args, **kwargs):
        return HttpResponse('Checkout')
