#coding:utf-8
__author__ = 'jc'
from django.contrib import admin
from .models import *
class SiteAdmin(admin.ModelAdmin):
    pass
admin.site.register(SiteModel,SiteAdmin)
class BlogRollAdmin(admin.ModelAdmin):
    pass
admin.site.register(BlogRoll,BlogRollAdmin)

class ArchiveAdmin(admin.ModelAdmin):
    pass
admin.site.register(Archives,ArchiveAdmin)