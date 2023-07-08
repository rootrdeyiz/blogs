from django.urls import path
from .views import Anasayfa, AnaHaberCreate, blog_detail, index, iletisim_form_view,login,register,market
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', Anasayfa.as_view(), name='anasayfa'),
    path('Haberler/<str:url>/', views.blog_detail, name='blog_detail'),
    path('', index, name='index'),
    path('arama/', views.arama, name='arama'),
    path('bagisyap/', views.bagısyap, name='bagısyap'),
    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),
    path('iletisim/', iletisim_form_view, name='iletisim'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('market/', views.market, name='market'),
    path('urun/<int:urun_id>/', views.urun_detail, name='urun_detail'),
    path('kategoriler/', views.categories, name='categories'),
    path('kategori/<int:kategori_id>/', views.kategori_view, name='kategori_view'),
    path('kategori-arama/', views.kategori_arama, name='kategori_arama'),
    path('Haberler/<str:slug>/', views.blog_detail, name='blog_detail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)