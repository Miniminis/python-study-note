from django import forms

class LoginForm(forms.Form):
    userEmail = forms.CharField(max_length=64, label="사용자 이름")
    userPw = forms.CharField(label="비밀번호", widget=forms.PasswordInput)