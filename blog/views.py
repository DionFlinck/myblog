from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from blog.models import Category, Banner,Article
from .models import Article


def hello(request):
    return HttpResponse('欢迎使用Django!')


def index(request):
    allcategory = Category.objects.all()
    banner = Banner.objects.filter(is_active=True)[0:4]
    tui=Article.objects.filter(tui_id=1)[:3]
    allarticle=Article.objects.all().order_by('-id')[0:10]
    context = {
        'allcategory': allcategory,
        'banner': banner,
        'tui':tui,
        'allarticle':allarticle,
    }
    return render(request, 'index.html', context)


def list(request, lid):
    pass


def show(request, sid):
    pass


def tag(request, tag):
    pass


def search(request):
    pass


def about(request):
    pass
