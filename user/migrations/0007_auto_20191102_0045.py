# Generated by Django 2.2.4 on 2019-11-01 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20191030_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(blank=True, default="'Belirtilmedi", max_length=20, null=True, verbose_name='Bulunduğunuz Şehir'),
        ),
    ]
