# Generated by Django 4.2 on 2023-06-19 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0008_alter_anahaber_baslik'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='banners/')),
                ('caption', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
