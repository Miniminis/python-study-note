from django import forms

class ProductCreateForm(forms.Form):
    name = forms.CharField(
        error_messages={
            'required' : '상품명을 입력해주세요!'
        },
        max_length=256,
        label='상품명'
    )
    price = forms.IntegerField(
        error_messages={
            'required' : '상품가격 입력해주세요!'
        },
        label='가격'
    )
    description = forms.CharField(
        error_messages={
            'required' : '상품에 대해 설명해주세요!'
        },
        label='상세설명'
    )
    stuck = forms.IntegerField(
        error_messages={
            'required' : '재고량을 입력해주세요!'
        },
        label='재고수량'
    )

    def clean(self):
        cleaned_data = super().clean()
        typed_name = cleaned_data.get('name')
        typed_price = cleaned_data.get('price')
        typed_description = cleaned_data.get('description')
        typed_stuck = cleaned_data.get('stuck')

        if not (typed_name and typed_price and typed_description and typed_stuck):
            self.add_error('name', '상품명이 없습니다.')
            self.add_error('price', '상품 가격이 없습니다!')

