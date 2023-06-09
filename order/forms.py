from django import forms
from django.contrib.auth.models import User
from django.db import transaction

from .models import Order
from product.models import Product


class OrderForm(forms.Form):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    quantity = forms.IntegerField(
        error_messages={'required': "수량을 입력하세요."},
        label="수량"
    )
    product = forms.IntegerField(
        error_messages={'required': "상품을 입력하세요."},
        label="상품", widget=forms.HiddenInput # 화면에는 보이지 않는 인풋
    )

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')
        fcuser = self.request.user

        if quantity and product and fcuser:
            with transaction.atomic():
                prod = Product.objects.get(pk=product)
                order = Order(
                    quantity=quantity,
                    product=Product.objects.get(pk=product),
                    fcuser=User.objects.get(username=fcuser)
                )

                # 수량만큼 재고에서 차감
                if (prod.stock>=order.quantity):
                    prod.stock -= quantity
                    prod.save()
                    order.save()
                else:
                    self.add_error('quantity', "수량이 없습니다.")

        else:
            self.product = product
            self.add_error('quantity', '값이 없습니다')
            self.add_error('product', '값이 없습니다')
