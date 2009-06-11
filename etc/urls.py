from django.conf.urls.defaults import *


urlpatterns = patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Working/library/projects/etc/media'}),
    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'index.html'}),
    url(r'^(?P<path>.*)$', 'etc.views.page'),
)