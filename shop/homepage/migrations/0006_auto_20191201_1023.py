# Generated by Django 2.2.7 on 2019-12-01 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_auto_20191201_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotdeal',
            name='time_deal',
            field=models.CharField(editable=False, max_length=50),
        ),
    ]