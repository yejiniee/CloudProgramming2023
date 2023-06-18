
from django.contrib.auth.models import User
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 32, verbose_name="상품명")
    price = models.IntegerField(verbose_name = "상품가격")
    description = models.TextField(verbose_name="상품설명")
    head_image = models.ImageField(verbose_name="썸네일", upload_to='product/images/%Y/%m/%d/')
    stock = models.IntegerField(verbose_name="재고")
    registered_date = models.DateTimeField(verbose_name="등록시간", auto_now_add=True)


    def __str__(self):
        return f'[{self.pk}] {self.name}'

    def get_absolute_url(self):
        return f'/product/{self.pk}/'

    class Meta:
        db_table = 'shop_product'
        verbose_name = '상품'
        verbose_name_plural = '상품'


