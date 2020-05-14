from django.db import models

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='고객')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='제품')
    quantity = models.IntegerField(verbose_name='수량') 
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='주문날짜')

    def __str__(self):
        return str(self.user) + " : " + str(self.product)

    class Meta:
        db_table = 'aboutfit_order'
        verbose_name = 'aboutfit order'
        verbose_name_plural = 'aboutfit order group'