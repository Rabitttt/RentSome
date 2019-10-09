from django.db import models

# Create your models here.

class ProductModel(models.Model):
    name = models.CharField(max_length=30,name="Ürün")
    
