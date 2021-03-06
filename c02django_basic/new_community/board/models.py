from django.db import models

# Create your models here.
class NewBoard(models.Model):
    title = models.CharField(
        max_length=128, 
        verbose_name='제목'
    )
    content = models.TextField(
        verbose_name='내용'
    )
    writer = models.ForeignKey(
        'new_user.NewUser', 
        on_delete=models.SET_NULL, 
        null=True, 
        verbose_name='작성자'
    )
    reg_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='작성시간'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'new_community_board'
        verbose_name='뉴 커뮤니티 게시글'
        verbose_name_plural = '뉴 커뮤니티 게시글 모음'


    

