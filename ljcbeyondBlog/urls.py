from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

admin.autodiscover()

from .views import index

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'ljcbeyondBlog.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^index/', index,name='index'),
                       url(r'^$', index),
                       url(r'article/(?P<title>\S+)/$','article.views.detail'),
                       url(r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/$','article.views.archive'),
                       url(r'^category/(?P<category>\S+)/$','article.views.category'),
                      # url(r'^reading/$','article.views.reading'),
                      # url(r'^about/$','article.views.about'),
                       # url(r'^crawlfromgithub/$','article.crawl.cronjob'),
                       )
import os

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
