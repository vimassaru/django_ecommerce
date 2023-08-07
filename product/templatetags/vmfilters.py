from django.template import Library
from utils import utils

register = Library()


@register.filter
def price_formatted(value):
    return utils.us_price_formatted(value)


@register.filter
def total_shop_cart_amount(shop_cart):
    return utils.total_shop_cart_amount(shop_cart)


@register.filter
def cart_totals(shop_cart):
    return utils.cart_totals(shop_cart)
