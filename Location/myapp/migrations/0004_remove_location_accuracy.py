# Generated by Django 2.1 on 2018-12-01 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20181201_1958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='accuracy',
        ),
    ]
