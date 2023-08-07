def us_price_formatted(value):
    return f'USD$ {value:.2f}'


def total_shop_cart_amount(shop_cart):
    return sum([item['amount'] for item in shop_cart.values()])


def cart_totals(shop_cart):
    return sum(
        [
            item.get('quantitative_off_price')
            if item.get('quantitative_off_price')
            else item.get('quantitative_price')
            for item
            in shop_cart.values()
        ]
    )
