# Generated by Django 2.2.7 on 2019-11-30 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_auto_20191130_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='features', to='products.Product'),
        ),
    ]
