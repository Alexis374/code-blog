# coding:utf-8
from django.db import models


class Article(models.Model):
    title = models.CharField(u'标题', max_length=50)
    pub_time = models.DateTimeField(u'发布时间', )
    author = models.CharField(u'作者', max_length=10)
    text = models.TextField(u'正文')
    tag = models.ManyToManyField('Tag', verbose_name=u'标签')
    category = models.ForeignKey('Category', verbose_name=u'类别')

    def __unicode__(self):
        return self.title

    def get_url(self):
        return u'/article/{}'.format(self.title)

    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    name = models.CharField(u'标签名', max_length=20)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'标签'
        verbose_name_plural = verbose_name


class Category(models.Model):
    name = models.CharField(u'类别名', max_length=20)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'类别'
        verbose_name_plural = verbose_name
