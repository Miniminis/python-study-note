from django.db import models

# Create your models here.
# sqlite3 db.sqlite3 : 테이블 생성 확인

class HelloUser(models.Model):
    username = models.CharField(max_length=64, verbose_name='사용자명')
    userpw = models.CharField(max_length=64, verbose_name='비밀번호')
    regdate = models.DateTimeField(auto_now_add=True, verbose_name='가입날짜')

    def __str__(self):    # 클래스 자체를 문자열로 변환했을때 호출되는 함수
        return self.username

    class Meta:
        db_table = 'hellousers'
        verbose_name = '헬로 커뮤니티 유저'
        verbose_name_plural = '헬로 커뮤니티 유저들'

