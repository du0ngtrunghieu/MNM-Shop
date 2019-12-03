# Generated by Django 2.2.7 on 2019-12-01 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_auto_20191201_0641'),
        ('homepage', '0012_remove_hotdeal_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotdeal',
            name='product',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.Product'),
        ),
    ]
