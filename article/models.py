#coding:utf-8
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(u'标题',max_length=50)
    pub_time = models.DateTimeField(u'发布时间',)
    author = models.CharField(u'作者',max_length=10)
    text = models.TextField(u'正文')
