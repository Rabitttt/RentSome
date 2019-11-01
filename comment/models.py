from django.db import models
from user.models import User
from product.models import ProductModel
# Create your models here.

class Comment(models.Model):
    comment = models.CharField(max_length=300 , verbose_name="Yorum")
    sender = models.ForeignKey(User,on_delete= models.SET_NULL,null=True,related_name="user")
    reciever = models.ForeignKey(ProductModel,on_delete=models.CASCADE,related_name="product")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender

class NestedComment(Comment):
    nested = models.ForeignKey(Comment,on_delete=models.DO_NOTHING,related_name="yorum")
