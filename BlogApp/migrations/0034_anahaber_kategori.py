# Generated by Django 4.2 on 2023-06-23 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0033_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='anahaber',
            name='kategori',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gonderiler', to='BlogApp.category'),
        ),
    ]
