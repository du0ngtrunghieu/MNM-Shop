# Generated by Django 2.2.7 on 2019-12-01 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_auto_20191201_0638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productfamily',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productfamily', to='categories.ProductFamily'),
        ),
        migrations.DeleteModel(
            name='ProductFamily',
        ),
    ]