import os.path

from django.contrib.auth.models import User
from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)

    def get_absolute_url(self):
        return f'/product/category/{self.slug}/'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Product_Categories'


class Product(models.Model):
    name = models.CharField(max_length = 32, verbose_name="상품명")
    price = models.IntegerField(verbose_name = "상품가격")
    description = models.TextField(verbose_name="상품설명")
    stock = models.IntegerField(verbose_name="재고")
    registered_date = models.DateTimeField(verbose_name="등록시간", auto_now_add=True)
    #category = models.ForeignKey(ProductCategory, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}] {self.name}'

    def get_absolute_url(self):
        return f'/product/{self.pk}/'


