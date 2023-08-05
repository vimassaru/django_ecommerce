# Generated by Django 4.2.4 on 2023-08-05 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='marketing_off_price',
            field=models.FloatField(default=0, verbose_name='Off Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='marketing_price',
            field=models.FloatField(verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(blank=True, default='name', max_length=255),
        ),
    ]
