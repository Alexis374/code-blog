__author__ = 'ljcbeyond'
from django.http import HttpResponse
from django.shortcuts import render
from .models import SiteModel,Archives,BlogRoll
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from article.models import *
def get_basic_info():
    sitemodel = SiteModel.objects.all()[0]
    blogrolls = BlogRoll.objects.filter(sitemodel=sitemodel)
    archives = Archives.objects.all()
    categories = Category.objects.all()
    context = dict(title=sitemodel.site_title,blogrolls=blogrolls,archives=archives,categories=categories)
    return context

def index(request):
    context = get_basic_info()
    allarticles = Article.objects.all()
    paginator = Paginator(allarticles,10)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    context['articles'] = articles
    return render(request, 'blog/articles.html',context)