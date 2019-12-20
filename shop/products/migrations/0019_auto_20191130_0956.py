# Generated by Django 2.2.7 on 2019-11-30 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_product_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='label',
            field=models.CharField(blank=True, choices=[('N', 'News'), ('H', 'Hot'), ('T', 'Trend')], max_length=20, null=True),
        ),
    ]