from django.conf.urls.defaults import *
from etc.settings import PROJECT_DIR, DEBUG

urlpatterns = patterns('',
)

if DEBUG == True:
    urlpatterns += patterns('',
		url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': PROJECT_DIR + '/media'}),
	)

urlpatterns += patterns('',
    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'index.html'}),
	# The next two lines redirect to our old forms temporarily
	url(r'^faculty_request_form.html$', 'etc.views.tempredirect', {'path': 'old/request.htm'}),
	url(r'^service_request.html$', 'etc.views.tempredirect', {'path': 'old/report_problem.htm'}),
	# url(r'^service_request.html$', 'etc.views.service'),
    url(r'^(?P<path>.*)$', 'etc.views.page'),
)