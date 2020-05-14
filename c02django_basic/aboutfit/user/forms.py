from django import forms
from django.contrib.auth.hashers import check_password
from .models import User

class RegisterForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required' : '이메일을 입력해주세요!'
        },
        max_length=64, label='이메일'
    )

    pw = forms.CharField(
        error_messages={
            'required' : '비밀번호를 입력해주세요!',
            'invalid' : '이메일 형식으로 입력해주세요!'
        },
        widget=forms.PasswordInput,
        label='비밀번호'
    )
    
    repw = forms.CharField(
        error_messages={
            'required' : '비밀번호 확인을 입력해주세요!'
        },
        widget=forms.PasswordInput,
        label='비밀번호 확인'
    )

    def clean(self):
        cleaned_data = super().clean()
        in_email = cleaned_data.get('email')
        in_pw = cleaned_data.get('pw')
        in_repw = cleaned_data.get('repw')

        if in_pw and in_repw:
            if in_pw != in_repw:
                self.add_error('repw', '비밀번호가 서로 다릅니다!')
            else :
                user = User(
                    email=in_email, 
                    password=in_pw
                )
                user.save()
        
        


        

       
