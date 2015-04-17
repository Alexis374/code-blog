from django.shortcuts import render
from .models import Article, Category
from django.shortcuts import get_list_or_404, get_object_or_404
from ljcbeyondBlog.views import get_basic_info
import datetime
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


def detail(request, title):
    context = get_basic_info()
    article = get_object_or_404(Article, title=title)
    context['article'] = article
    return render(request, 'detail.html', context
                  )


def archive(request, year, month):
    year = int(year)
    month = int(month)
    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year
    this_month_date = datetime.datetime.strptime('{0} {1}'.format(year, month), '%Y %m')
    next_month_date = datetime.datetime.strptime('{0} {1}'.format(next_year, next_month), '%Y %m')
    allarticles = get_list_or_404(Article, pub_time__range=(this_month_date, next_month_date))
    context = get_basic_info()
    paginator = Paginator(allarticles,10)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    context['articles'] = articles
    return render(request, 'blog/articles.html', context)


def category(request, category):
    category = Category.objects.get(name=category)
    allarticles = get_list_or_404(Article, category=category)
    context = get_basic_info()
    paginator = Paginator(allarticles,10)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    context['articles'] = articles
    return render(request, 'blog/articles.html', context)
