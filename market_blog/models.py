from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Atik(models.Model):
    non_pwodui = models.CharField(max_length=100, default='Non Pwodui a')
    slug = models.SlugField(unique=True, max_length=255, default='slug')
    deskripsyon = models.TextField(default='Deskripsyon pwodui a')
    specs = models.CharField(max_length=255, default='Kek lot detay sou pwodui a')
    uploaded = models.DateField(auto_now_add=True, verbose_name='Pwodui sa online depi')
    published = models.BooleanField(default=True)
    seller = models.CharField(max_length=75, default='Moun kap vann nan')
    kontak = models.CharField(max_length=11, default='Nimewo telefon ou')
    pri = models.IntegerField(default='Pri pwodui a an HTG')
    end_date = models.DateField(['%Y-%m-%d %H:%M:%S'], null=True)
    foto_atik = models.ImageField('img', upload_to='img_atik/', blank=True)

    def __str__(self):
        return self.non_pwodui

    class Meta:
        ordering = ['uploaded']

    def __unicode__(self):
        return u'%s' % self.non_pwodui

    def get_absolute_url(self):
        return reverse('market_blog.views.atik', args=[self.slug])