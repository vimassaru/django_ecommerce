# Generated by Django 4.2.4 on 2023-08-04 21:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('status', models.CharField(choices=[('A', 'Approved'), ('C', 'Created'), ('R', 'Declined'), ('P', 'Pending'), ('S', 'Sent'), ('F', 'Finished')], default='C', max_length=1)),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('variation', models.CharField(max_length=255)),
                ('varitation_id', models.PositiveIntegerField()),
                ('marketing_price', models.FloatField()),
                ('marketing_off_price', models.FloatField(default=0)),
                ('image', models.CharField(max_length=2000)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
            ],
            options={
                'verbose_name': 'Order Item',
                'verbose_name_plural': 'Items Order',
            },
        ),
    ]
