from django import forms
from .models import Product

class RegisterForm(forms.Form):
    name = forms.CharField(
        error_messages={
            'required': '상품명을 입력해주세요.'
        },
        max_length=64, label='상품'
    )
    price = forms.IntegerField(
        error_messages={
            'required': '상품가격을 입력해주세요.'
        },
        label='상품가격'
    )
    description = forms.CharField(
        error_messages={
            'required': '상품설명을 입력해주세요.'
        }, label='상품명'
    )
    stock = forms.IntegerField(
        error_messages={
            'required': '재고를 입력해주세요.'
        }, label='재고'
    )

    def clean(self):
        cleaned_date = super().clean()
        name = cleaned_date.get('name')
        price = cleaned_date.get('price')
        description = cleaned_date.get('description')
        stock = cleaned_date.get('stock')

        if name and price and description and stock :
            prodoct = Product(
                name = name,
                price = price,
                description = description,
                stock = stock
            )
            prodoct.save()

