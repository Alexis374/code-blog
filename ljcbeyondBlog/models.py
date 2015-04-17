# coding:utf-8
from django.db.models import Model, CharField, ForeignKey, URLField, IntegerField


class SiteModel(Model):
    site_title = CharField(u'网站标题', max_length=20)

    def __unicode__(self):
        return self.site_title

    class Meta:
        verbose_name = u'站点管理'
        verbose_name_plural = verbose_name


class BlogRoll(Model):
    name = CharField(u'标题', max_length=20)
    url = URLField(u'url', max_length=100)
    sitemodel = ForeignKey(SiteModel)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'友情站点'
        verbose_name_plural = verbose_name


class Archives(Model):
    year = IntegerField(u'年')
    month = IntegerField(u'月')
    num = IntegerField(u'文章数量')

    def __unicode__(self):
        if self.month < 10:
            return u'{0}年0{1}月({2})'.format(self.year, self.month, self.num)
        return u'{0}年{1}月({2})'.format(self.year, self.month, self.num)

    class Meta:
        ordering = ['year', 'month']
        verbose_name_plural = u'存档'
        verbose_name = verbose_name_plural