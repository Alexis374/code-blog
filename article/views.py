from django.shortcuts import render
from .models import Article
from django.shortcuts import get_object_or_404
from ljcbeyondBlog.views import get_basic_info
def detail(request,title):
    context = get_basic_info()
    article = get_object_or_404(Article,title=title)
    context['article'] = article
    return render(request,'detail.html',context
                  )