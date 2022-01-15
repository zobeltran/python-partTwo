from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Stock(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return self.name


class StockOrder(models.Model):
    id = models.IntegerField
    # user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user')
    stock = models.ForeignKey(
        Stock, on_delete=models.CASCADE, related_name='stock')
    quantity = models.IntegerField(default=0)
    total_price = models.FloatField(default=0)

    @property
    def total_price(self):
        computed_price = self.quantity * self.stock.price
        return computed_price

    def __str__(self):
        return self.stock.name


class UserPortfolio(models.Model):
    id = models.IntegerField
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='user')
    stock_order = models.ManyToManyField(
        StockOrder, related_name='stock_order')
    total_amount = models.FloatField(default=0)

    @property
    def total_amount(self):
        computed_amount = sum(self.stockOrder.total_price)
        return computed_amount

    def __str__(self):
        return self.user.username
