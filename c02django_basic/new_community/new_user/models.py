from django.db import models

# Create your models here.

class NewUser(models.Model):
    username = models.CharField(max_length=32, verbose_name='사용자명')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='가입시간')

    # 어드민에서 보이는 유저네임 : 클래스의 이름을 문자열로 변환한 것. 
    # 파이썬 내부에는 클래스 >> 문자열로 변환할때 어떻게 변환할 지 결정할 수 있는 내장함수 __str__() 가 존재함.
    # username 을 반환하도록 설정해줌 
    def __str__(self):
        return self.username    

    # 테이블 명 직접 설정하기
    class Meta:
        db_table = 'newcommunity_user'
        verbose_name = '새커뮤니티 사용자'
        verbose_name_plural = '새커뮤니티 사용자'
