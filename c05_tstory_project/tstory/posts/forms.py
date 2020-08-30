from django import forms
from .models import TComment

class PostForm(forms.Form):
    title = forms.CharField(
        error_messages={
            'required' : '제목을 입력해주세요!'
        },
        max_length=255
    )
    content = forms.CharField(
        error_messages={
            'required' : '내용을 입력해주세요!'
        }
    ) 
    image = forms.FileField(
        required=False
    )

    def clean(self):
        cd = super().clean()
        title = cd.get('title')
        content = cd.get('content')

        if not (title and content):
            self.add_error('title', '필수 항목입니다.')
            self.add_error('content', '필수 항목입니다.')


class CommentForm(forms.ModelForm):

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    post = forms.IntegerField(
        widget=forms.HiddenInput
    )

    class Meta:
        model = TComment
        fields = ['comment']




