# Generated by Django 4.2 on 2023-06-26 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0037_anahaber_tarih'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anahaber',
            old_name='tarih',
            new_name='tarihi',
        ),
    ]