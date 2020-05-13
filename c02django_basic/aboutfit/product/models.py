from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name='상품명')
    price = models.IntegerField(max_length=32, verbose_name='상품가격')
    stuck = models.IntegerField(max_length=32, verbose_name='상품재고')
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    class Meta:
        db_table = 'aboutfit_product'
        verbose_name = 'aboutfit product'
        verbose_name_plural = 'aboutfit product group'
