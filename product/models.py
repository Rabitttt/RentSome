from django.db import models

from user.models import User
# Create your models here.

class ProductModel(models.Model):
    name = models.CharField(max_length=30,verbose_name="Ürün Adı")
    price = models.FloatField(verbose_name='Fiyat',default=0)
    hire_date = models.DateTimeField(verbose_name='Kiralama Tarihii',auto_now_add=True)
    hire_end_date = models.DateTimeField(verbose_name="Kiralık Bitiş Tarihi",auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="product",related_name="owner")

    def __str__(self):
        return self.name
