# Generated by Django 4.2 on 2023-06-19 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0004_alter_gonder_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnaHaber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=120)),
                ('yazi', models.TextField(max_length=90000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Gonder',
        ),
    ]
