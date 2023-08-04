from django.db import models
from django.contrib.auth.models import User

"""
Order:
    user: FK User
    total: Float
    status: Choices
        ('A', 'Approved'),
        ('C', 'Created'),
        ('R', 'Declined'),
        ('P', 'Pending'),
        ('S', 'Sent'),
        ('F', 'Finished'),
"""


class Order(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    status = models.CharField(
        default="C",
        max_length=1,
        choices=(
            ('A', 'Approved'),
            ('C', 'Created'),
            ('R', 'Declined'),
            ('P', 'Pending'),
            ('S', 'Sent'),
            ('F', 'Finished'),
        )
    )

    def __str__(self) -> str:
        return f'Order num. {self.pk}'


"""
OrderItem:
    order: FK pedido
    product: Char
    product_id: Int
    variation: Char
    variation_id: Int
    marketing_price: Float
    marketing_off_price: Float
    amount: Int
    image: Char
"""


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    variation = models.CharField(max_length=255)
    varitation_id = models.PositiveIntegerField()
    marketing_price = models.FloatField()
    marketing_off_price = models.FloatField(default=0)
    image = models.CharField(max_length=2000)

    def __str__(self) -> str:
        return f'Item of {self.order}'

    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Items Order'
