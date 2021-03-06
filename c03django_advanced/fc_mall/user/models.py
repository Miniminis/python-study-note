from django.db import models

# Create your models here.
class FcUser(models.Model):
    email = models.EmailField(verbose_name='이메일')
    pw = models.CharField(max_length = 128, verbose_name='비밀번호')
    level = models.CharField(max_length=8, verbose_name='회원등급', choices=(
        ('admin', 'admin'),
        ('user', 'user'),
    ), default='user')
    regdate = models.DateTimeField(auto_now_add=True, verbose_name='가입일')

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'fc_user'
        verbose_name='사용자'
        verbose_name_plural='사용자'
