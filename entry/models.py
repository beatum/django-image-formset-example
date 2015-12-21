# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from sorl.thumbnail.fields import ImageField


class Entry(models.Model):
    """
    Description: Model Description
    """
    title = models.CharField(max_length=170)
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('entry_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ('-pk',)


class Picture(models.Model):
    """
    Description: Model Description
    """
    title = models.CharField(max_length=170)
    entry = models.ForeignKey(Entry, null=True, blank=True)
    image = ImageField(upload_to='upload')

    def __unicode__(self):
        return '%s' % self.title

    @models.permalink
    def get_absolute_url(self):
        return reverse('entry_new', kwargs={'pk': self.pk})


    def save(self, *args, **kwargs):
        super(Picture, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-pk',)
