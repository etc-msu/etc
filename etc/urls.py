from django.conf.urls.defaults import *
from etc.settings import PROJECT_DIR

urlpatterns = patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': PROJECT_DIR + '/media'}),
    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'index.html'}),
	url(r'^faculty_request_form.html$', 'etc.views.tempredirect', {'path': 'request'}),
	url(r'^service_request.html$', 'etc.views.tempredirect', {'path': 'report_problem'}),
	# url(r'^service_request.html$', 'etc.views.service'),
    url(r'^(?P<path>.*)$', 'etc.views.page'),
)