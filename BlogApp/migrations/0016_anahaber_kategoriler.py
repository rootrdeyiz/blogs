# Generated by Django 4.2 on 2023-06-20 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0015_kategori_ekle'),
    ]

    operations = [
        migrations.AddField(
            model_name='anahaber',
            name='kategoriler',
            field=models.ManyToManyField(to='BlogApp.kategori_ekle'),
        ),
    ]