# Generated by Django 2.2.7 on 2019-12-01 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_auto_20191201_1023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotdeal',
            old_name='products',
            new_name='product',
        ),
    ]
