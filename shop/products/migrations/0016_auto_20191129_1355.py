# Generated by Django 2.2.7 on 2019-11-29 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20191129_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(verbose_name='Giá'),
        ),
    ]
