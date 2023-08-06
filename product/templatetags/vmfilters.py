from django.template import Library
from utils import utils

register = Library()


@register.filter
def price_formatted(value):
    return utils.us_price_formatted(value)
