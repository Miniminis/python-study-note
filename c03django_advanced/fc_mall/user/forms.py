from django import forms
from .models import FcUser
from django.contrib.auth.hashers import check_password

class RegisterForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required' : '이메일을 입력해주세요!'
        },
        max_length=64, 
        label='이메일'
    )
    pw = forms.CharField(
        error_messages={
            'required' : '비밀번호를 입력해주세요!'
        },
        max_length=128,
        label='비밀번호', 
        widget=forms.PasswordInput
    )
    re_pw = forms.CharField(
        error_messages={
            'required' : '비밀번호를 입력해주세요!'
        },
        max_length=128, 
        label='비밀번호 확인',
        widget=forms.PasswordInput
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        pw = cleaned_data.get('pw')
        re_pw = cleaned_data.get('re_pw')

        if email and pw and re_pw:
            if pw != re_pw:
                self.add_error('re_pw', '비밀번호가 서로 다릅니다')


class LoginForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required' : '이메일을 입력해주세요!'
        },
        max_length=64,
        label='이메일'
    ) 
    pw = forms.CharField(
        error_messages={
            'required' : '비밀번호를 입력해주세요!'
        },
        label='비밀번호',
        max_length=128,
        widget=forms.PasswordInput
    )

    def clean(self):
        cleaned_data = super().clean()
        typed_email = cleaned_data.get('email')
        typed_pw = cleaned_data.get('pw')

        if typed_email and typed_pw:
            try:
                fcuser = FcUser.objects.get(email=typed_email)
            except FcUser.DoesNotExist:
                self.add_error('email', '일치하는 아이디가 없습니다!')
                return
            
            if not check_password(typed_pw, fcuser.pw):
                self.add_error('pw', '일치하는 비밀번호가 없습니다!')


            




