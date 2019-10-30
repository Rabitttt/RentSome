from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
# Create your models here.

class User(AbstractUser):
    location = models.CharField(max_length=20,null=True,blank=True,verbose_name='Bulunduğunuz Şehir')
    profile_picture = models.ImageField(null=True,blank=True,verbose_name='Profil Resmi')
    money = models.FloatField(verbose_name='Para',default=0,
                              validators=[
                                  MinValueValidator(0),
                              ])

    def __str__(self):
        return self.username
