# Generated by Django 2.1 on 2018-12-01 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='longitutde',
            new_name='longitude',
        ),
    ]
