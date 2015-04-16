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
                       url(r'^index/', index),
                       url(r'^$', index),
                       url(r'article/(?P<title>\S+)/$','article.views.detail')
                       )
import os

if settings.DEBUG:
    # raise IndexError,os.path.join(settings.BASE_DIR,'static')
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
