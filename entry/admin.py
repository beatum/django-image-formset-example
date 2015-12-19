from __future__ import unicode_literals
# -*- coding: utf-8 -*-
from django.contrib import admin

from models import Entry, Picture


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'owner')


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'entry',)
