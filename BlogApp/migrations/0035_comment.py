# Generated by Django 4.2 on 2023-06-23 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0034_anahaber_kategori'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icerik', models.TextField()),
                ('tarih', models.DateTimeField(auto_now_add=True)),
                ('haber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BlogApp.anahaber')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
