# Generated by Django 2.2.7 on 2019-12-01 10:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20191201_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotdeal',
            name='start_deal',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
