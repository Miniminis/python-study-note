from django import forms

class BoardForm(forms.Form):
    title = forms.CharField(
        max_length=128,
        label = '제목',
        error_messages={
            'required' : '글의 제목을 입력해주세요!'
        }
    )
    content = forms.CharField(
        label = '내용', 
        error_messages={
            'required' : '내용을 입력해주세요!'
        },
        widget=forms.Textarea
    )
