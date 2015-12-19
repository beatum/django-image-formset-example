from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from settings import MEDIA_ROOT


urlpatterns = patterns('',
    url(r'^entry/', include('entry.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


# This is only needed when using runserver in debug mode.
urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',  # NOQA
       {'document_root': MEDIA_ROOT, 'show_indexes': True}),
) + staticfiles_urlpatterns() + urlpatterns  # NOQA
