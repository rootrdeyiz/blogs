# Generated by Django 4.2 on 2023-06-19 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0010_alter_banner_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Banner',
        ),
    ]