# Generated by Django 2.2.7 on 2019-12-08 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0019_hotdeal_start_deal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotdeal',
            name='time_deal',
        ),
        migrations.AlterField(
            model_name='hotdeal',
            name='start_deal',
            field=models.DateTimeField(verbose_name='Ngày bắt đầu giảm giá'),
        ),
    ]
