# Generated by Django 3.1 on 2020-08-14 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0005_auto_20200814_1818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='sub_genre',
        ),
    ]
