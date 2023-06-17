from django import forms
from .models import Product

class RegisterForm(forms.Form):

    name = forms.CharField(
        error_messages={'required':"상품명을 입력하세요."},
        max_length = 32, label = "상품명"
    )
    price = forms.IntegerField(
        error_messages={'required' : "가격을 입력하세요."},
        label = "가격"
    )
    stock = forms.IntegerField(
        error_messages={'required':"수량을 입력하세요"},
        label = "재고"
    )
    description = forms.CharField(
        error_messages={'required':"상품 설명을 입력하세요"},
        label = "상품 설명"
    )

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        price = cleaned_data.get('price')
        stock = cleaned_data.get('stock')
        description = cleaned_data.get('description')
        
        if name and price and description and stock:
            product = Product(
                name=name,
                price=price,
                description=description,
                stock=stock
            )
            product.save()

