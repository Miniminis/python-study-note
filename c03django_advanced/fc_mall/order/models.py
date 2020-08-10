from django.db import models

# Create your models here.
class FcMallOrder(models.Model):
    fcuser = models.ForeignKey('user.FcUser', on_delete=models.CASCADE, verbose_name='주문자명')
    product = models.ForeignKey('product.FcMallProduct', on_delete=models.CASCADE, verbose_name='주문상품')
    quantity = models.IntegerField(verbose_name='주문수량')
    regdate = models.DateTimeField(auto_now_add=True, verbose_name='주문시간')

    def __str__(self):
        return str(self.fcuser) + ' : ' + str(self.product)
    
    class Meta:
        db_table = 'fcmall_order'
        verbose_name='주문'
        verbose_name_plural = '주문'