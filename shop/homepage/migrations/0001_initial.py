# Generated by Django 2.2.7 on 2019-12-01 09:55

from django.db import migrations, models
import django.db.models.deletion
import filebrowser.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0026_auto_20191201_0641'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumb1', filebrowser.fields.FileBrowseField(blank=True, max_length=5000, verbose_name='Image')),
                ('thumb2', filebrowser.fields.FileBrowseField(blank=True, max_length=5000, verbose_name='Image')),
                ('thumb3', filebrowser.fields.FileBrowseField(blank=True, max_length=5000, verbose_name='Image')),
                ('thumb4', filebrowser.fields.FileBrowseField(blank=True, max_length=5000, verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Slider',
                'verbose_name_plural': 'Sliders',
            },
        ),
        migrations.CreateModel(
            name='HotDeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_deal', models.DateTimeField(auto_now=True, verbose_name='Ngày bắt đầu')),
                ('end_deal', models.DateTimeField(verbose_name='Ngày hết')),
                ('available', models.BooleanField(default=True)),
                ('time_deal', models.DateTimeField(blank=True, editable=False)),
                ('products', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.Product')),
            ],
            options={
                'verbose_name': 'HotDeal',
                'verbose_name_plural': 'HotDeals',
            },
        ),
    ]
