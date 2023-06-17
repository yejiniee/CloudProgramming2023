from django.db import models
from django.contrib.auth.models import User

from product.models import Product


class Order(models.Model):
    fcuser = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")
    quantity = models.IntegerField(verbose_name="수량")

    def __str__(self):
        return str(self.fcuser) + ' ' + str(self.product)

    class Meta:
        db_table = 'shop_order'
        verbose_name = '주문'
        verbose_name_plural = '주문'