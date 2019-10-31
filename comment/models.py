from django.db import models
from user.models import User
from product.models import ProductModel
# Create your models here.

class Comment(models.Model):
    sender = models.ForeignKey(User,on_delete= models.SET_NULL,null=True)
    reciever = models.ForeignKey(ProductModel,on_delete=models.CASCADE,related_name="product")
    comment = models.TextField(verbose_name="Yorum")


class NestedComment(Comment):
    nested = models.ForeignKey(Comment,on_delete=models.DO_NOTHING,related_name="yorum")
