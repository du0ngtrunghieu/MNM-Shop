# Generated by Django 2.2.7 on 2019-12-26 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0022_auto_20191220_0801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialoffer',
            name='discount_price',
        ),
    ]
