from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import AnaHaber, Banner,Urun,Category,Gonderi
from django.views.generic.edit import CreateView
from .forms import AnaHaberForm,IletisimForm,CustomUserCreationForm, CustomAuthenticationForm
from django.shortcuts import render, get_object_or_404, redirect

def index(request):
    all_posts_list = AnaHaber.objects.all()
    categories = Category.objects.all()
    context = {
        'all_posts_list': all_posts_list,
        'categories': categories,
    }
    return render(request, 'index.html', context)

def kategori_arama(request):
    query = request.GET.get('q')  
    kategoriler = Category.objects.filter(name__icontains=query) if query else [] 

    context = {
        'query': query,
        'kategoriler': kategoriler
    }

    return render(request, 'kategori_arama.html', context)

def kategori_view(request, kategori_id):
    kategori = get_object_or_404(Category, id=kategori_id)
    gonderiler = kategori.gonderiler.all()
    return render(request, 'kategori_view.html', {'kategori': kategori, 'gonderiler': gonderiler})


def categories(request):
    categories = Category.objects.all()  
    context = {'categories': categories}
    return render(request, 'categories.html', context)

def urun_detail(request, urun_id):
    urun = get_object_or_404(Urun, id=urun_id)
    return render(request, 'urun_detail.html', {'urun': urun})

def market(request):
    urunler = Urun.objects.all()
    return render(request, 'market.html', {'urunler': urunler})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    logout(request)
    return redirect('home')

def iletisim_form_view(request):
    if request.method == 'POST':
        form = IletisimForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'iletisim/iletisim_basarili.html')
    else:
        form = IletisimForm()
    return render(request, 'iletisim/iletisim_formu.html', {'form': form})






class AnaHaberCreate(CreateView):
    model = AnaHaber
    form_class = AnaHaberForm 
    template_name = 'create_form.html'

class Anasayfa(ListView):
    model = AnaHaber
    template_name = "index.html"
    context_object_name = "all_posts_list"




def blog_detail(request, url):
    url = url.lower()
    blog = get_object_or_404(AnaHaber, url=url)
    return render(request, 'blog_detail.html', {'blog': blog})






def arama(request):
    query = request.GET.get('q')
    results = AnaHaber.objects.filter(baslik__icontains=query) 
    
    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'arama.html', context)



def bagısyap(request):
    return render(request, 'bagısyap.html')

def hakkimizda(request):
    return render(request, 'hakkimizda.html')