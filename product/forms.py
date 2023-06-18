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
    head_image = forms.ImageField(
        error_messages={'required': "썸네일 이미지를 입력하세요"},
        label="썸네일"
    )

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        price = cleaned_data.get('price')
        stock = cleaned_data.get('stock')
        description = cleaned_data.get('description')
        head_image = cleaned_data.get('head_image')
        
        if name and price and description and stock and head_image:
            product = Product(
                name=name,
                price=price,
                stock=stock,
                description=description,
                head_image=head_image,

            )
            product.save()

