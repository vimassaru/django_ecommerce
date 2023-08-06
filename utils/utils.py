def us_price_formatted(value):
    return f'USD$ {value:.2f}'


def total_shop_cart_amount(shop_cart):
    return sum([item['amount'] for item in shop_cart.values()])
