from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=64, verbose_name='이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='가입시간')

    class Meta:
        db_table = 'aboutfit_user'
        verbose_name = 'aboutfit user'
        verbose_name_plural = 'aboutfit user group'