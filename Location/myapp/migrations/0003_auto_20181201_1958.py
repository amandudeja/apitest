# Generated by Django 2.1 on 2018-12-01 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20181201_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.CharField(max_length=10),
        ),
    ]
