from django.conf.urls.defaults import *
from etc.settings import PROJECT_DIR, DEBUG

urlpatterns = patterns('',
)

if DEBUG == True:
    urlpatterns += patterns('',
		url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': PROJECT_DIR + '/media'}),
		url(r'^service_request.html$', 'etc.views.tempredirect', {'path': 'etcetera/service_form'}),
	)

if DEBUG == False:
	urlpatterns += patterns('',
		url(r'^service_request.html$', 'etc.views.tempredirect', {'path': 'old/report_problem.htm'}),
		url(r'^faculty_request_form.html$', 'etc.views.tempredirect', {'path': 'old/request.htm'}),
	)

urlpatterns += patterns('',
    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'index.html'}),
    url(r'^(?P<path>.*)$', 'etc.views.page'),
)