from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category,CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    pass
admin.site.register(Article,ArticleAdmin)
class TagAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tag,TagAdmin)
