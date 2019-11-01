# Generated by Django 2.2.4 on 2019-11-01 09:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0004_remove_comment_deneme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]