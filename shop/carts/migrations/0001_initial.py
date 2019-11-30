# Generated by Django 2.2.7 on 2019-11-30 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, verbose_name='Mã giảm giá')),
                ('amount', models.BigIntegerField(default=0, verbose_name='Số tiền giảm giá')),
            ],
        ),
    ]