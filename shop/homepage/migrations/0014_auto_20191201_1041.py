# Generated by Django 2.2.7 on 2019-12-01 10:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0013_hotdeal_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotdeal',
            name='start_deal',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 1, 10, 41, 33, 416124, tzinfo=utc), editable=False),
        ),
    ]