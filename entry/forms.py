# -*- coding: utf-8 -*-
"""
Created by Ivan Semernyakov on 18.12.15
Developer URL: http://beatum-site.ru/
Developer email: <direct@beatum-group.ru>
"""

from django.forms import ModelForm
from django import forms
from django.forms.models import inlineformset_factory
from django.contrib.auth.models import User
from models import Entry, Picture
from file_resubmit.admin import AdminResubmitImageWidget  # AdminResubmitFileWidget


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['title']


# Возможно эта форма лишняя
class PictureForm(ModelForm):
    class Meta:
        model = Picture
        widgets = {
            'image': AdminResubmitImageWidget
        }


# TODO: указать явно form=PictureForm и добавить сохранение пользователя
PictureFormSet = inlineformset_factory(Entry, Picture, fk_name='entry', max_num=12, extra=3,
                                       widgets={'image': AdminResubmitImageWidget})
