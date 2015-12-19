# -*- coding: utf-8 -*-
from django.conf.urls import url
from views import EntryCreateView, EntryUpdateView, EntryListView, EntryDeleteView

"""
Created by Ivan Semernyakov on 18.12.15
Developer URL: http://beatum-site.ru/
Developer email: <direct@beatum-group.ru>
"""

urlpatterns = (
    url(r'^list/$', EntryListView.as_view(), name='entry_list'),
    url(r'^create/$', EntryCreateView.as_view(), name='entry_add'),
    url(r'^update/(?P<pk>[0-9]+)/$', EntryUpdateView.as_view(), name='entry_update'),
    url(r'^delete/(?P<pk>[0-9]+)/$', EntryDeleteView.as_view(), name='entry_delete'),
)
