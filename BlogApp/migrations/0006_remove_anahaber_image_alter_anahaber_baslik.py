# Generated by Django 4.2 on 2023-06-19 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0005_anahaber_delete_gonder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anahaber',
            name='image',
        ),
        migrations.AlterField(
            model_name='anahaber',
            name='baslik',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
