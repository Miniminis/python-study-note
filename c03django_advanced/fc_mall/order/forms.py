from django import forms

class OrderCreateForm(forms.Form):

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    product = forms.IntegerField(
        error_messages={
            'required' : '주문하실 상품명을 입력해주세요!'
        },
        label='주문상품', 
        widget=forms.HiddenInput
    )
    quantity = forms.IntegerField(
        error_messages={
            'required' : '주문 수량을 입력해주세요!'
        },
        label='주문수량'
    )

    def clean(self):
        cleaned_data = super().clean()
        i_product = cleaned_data.get('product')
        i_quantity = cleaned_data.get('quantity')

        if not (i_product and i_quantity):
            self.add_error('product', '상품명이 없습니다!')
            self.add_error('quantity', '주문 수량이 없습니다!')



