# Generated by Django 4.2.4 on 2023-08-05 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_alter_userprofile_ssn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='extra_description',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]