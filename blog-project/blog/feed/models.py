from django.db import models

# Create your models here.
# blog db 구조 setting 
# 1. article 
# 2. comment 
# 3. hashtag 

class Article(models.Model):
    objects = models.Manager()
    CATEGORY_CHOICES = [
        ('DV', 'Development'),
        ('PS', 'Personal'),
        ('AF', 'Africa'),
    ]
    title = models.CharField(max_length=200, verbose_name="제목")
    content = models.TextField(verbose_name="본문내용")
    category = models.CharField(
        max_length=3,
        choices = CATEGORY_CHOICES,
        default = ('DV', 'Development'),
        verbose_name="카테고리"
    )

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, verbose_name="댓글작성자")
    content = models.CharField(max_length=200, verbose_name="댓글내용")

    def __str__(self):
        return "[{}] 에 대한 코멘트 : {} - by {}".format(self.article.title, self.content, self.username)    
   
class HashTag(models.Model):
    hashtag = models.CharField(max_length=50, verbose_name="해쉬태그")

    def __str__(self):
        return self.hashtag