from django.db import models
from user.models import User
# Create your models here.

class ProductModel(models.Model):
    name = models.CharField(max_length=30,verbose_name="Ürün Adı",null=False)
    price = models.FloatField(verbose_name='Fiyat',default=0)
    description = models.CharField(max_length=500,null=True,blank=True,verbose_name="Açıklama")
    product_image = models.ImageField(blank=True,null=True,verbose_name="Ürün Resmi Ekleyin")
    owner = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="product",related_name="owner")
    is_available = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True,null=True)
    hire_date = models.DateField(auto_now=True,null=True)
    hire_end_date = models.DateTimeField(verbose_name="Kiralık Bitiş Tarihi",null=True,auto_now_add=True)
    hirer = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name



#comment kısmı yazılacak (comment kısmı yazıldı nested comment yazılacak)
#kiralık tarihleri ayarlanacak (kira bitiş tarihi eklendi , en düşük değerin bugun olması sağlanacak.)
#(oluşturuldu)---ürünlerim kısmı detaylandırılacak (kiradakı , kiralanmayı bekleyen , kiraladıklarım)
#defult user degerleri atanacak
#profil güncelleme kısmında parola kısmı yapılacak
#kategoriler , arama , yorumları sıralama kısmı eklenecek
#butun projeye bootstrap eklenecek