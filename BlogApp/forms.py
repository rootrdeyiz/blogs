from django import forms
from .models import AnaHaber,Iletisim,CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class IletisimForm(forms.ModelForm):
    class Meta:
        model = Iletisim
        fields = ('konu_basligi', 'konu', 'e_posta')


class AnaHaberForm(forms.ModelForm):
        pass
