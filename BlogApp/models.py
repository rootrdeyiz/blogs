from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    

class CustomUser(AbstractUser):
    pass

class Urun(models.Model):
    urun_resmi = models.ImageField(upload_to='urunler/')
    urun_ismi = models.CharField(max_length=100)
    urun_aciklamasi = models.TextField()
    urun_fiyati = models.DecimalField(max_digits=8, decimal_places=2)
    stok_adedi = models.PositiveIntegerField()

    def __str__(self):
        return self.urun_ismi

class Gonderi(models.Model):
    kategori = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='gonderi')


class AnaHaber(models.Model):
    tarihi = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='Haber-Resimler/', null=True)
    baslik = models.CharField(max_length=120, unique=True)
    yazi = models.TextField(max_length=90000)
    url = models.CharField(max_length=255, null=True)
    kategori = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='gonderiler', blank=True, null=True)


    def get_absolute_url(self):
        return reverse('anahaber_detay', args=[str(self.url)])
    


    def __str__(self):
        return self.baslik[:60]



class Banner(models.Model):
    image = models.ImageField(upload_to='banners/')
    description = models.TextField()


class Iletisim(models.Model):
    konu_basligi = models.CharField(max_length=100)
    konu = models.TextField()
    e_posta = models.EmailField()

    def __str__(self):
        return self.konu_basligi

