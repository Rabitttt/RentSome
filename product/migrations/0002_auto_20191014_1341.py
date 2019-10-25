# Generated by Django 2.2.4 on 2019-10-14 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Ürün Adı'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='price',
            field=models.FloatField(default=0, verbose_name='Fiyat'),
        ),
    ]