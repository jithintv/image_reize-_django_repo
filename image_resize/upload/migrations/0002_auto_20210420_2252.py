# Generated by Django 3.2 on 2021-04-20 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='old_height',
        ),
        migrations.RemoveField(
            model_name='upload',
            name='old_width',
        ),
    ]
