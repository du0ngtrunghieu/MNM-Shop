# Generated by Django 2.2.7 on 2019-11-30 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20191130_0156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='postal_code',
        ),
    ]
