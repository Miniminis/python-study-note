from django import forms
from .models import NewUser
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    userEmail = forms.CharField(
        max_length=64, 
        label="사용자 아이디",
        error_messages= {
            'required' : '아이디를 입력해주세요!'
        }
    )
    userPw = forms.CharField(
        label="비밀번호", 
        widget=forms.PasswordInput,
        error_messages= {
            'required' : '비밀번호를 입력해주세요!'
        }
    )

    def clean(self):
        cleaned_data = super().clean()

        typed_email = cleaned_data.get('userEmail')
        typed_pw = cleaned_data.get('userPw')

        if typed_email and typed_pw:
            newuser = NewUser.objects.get(useremail=typed_email)
            if not check_password(typed_pw, newuser.password):
                self.add_error('password', '아이디 혹은 비밀번호를 확인해주세요!')
            else :
                self.user_id = newuser.id

