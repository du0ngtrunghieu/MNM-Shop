# Generated by Django 2.2.7 on 2019-12-01 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotdeal',
            name='start_deal',
            field=models.DateTimeField(verbose_name='Ngày bắt đầu'),
        ),
    ]
