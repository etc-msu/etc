from django.conf.urls.defaults import *
from etc.settings import PROJECT_DIR, DEBUG

urlpatterns = patterns('',
)

if DEBUG == True:
	urlpatterns += patterns('',
		url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': PROJECT_DIR + '/media'}),
		# This is what checkout will be soon
		url(r'^faculty_request_form.html$', 'etc.views.tempredirect', {'path': 'etcetera/checkout/form'}),
	)

if DEBUG == False:
	urlpatterns += patterns('',
		# Remove this line when checkout is done
		url(r'^faculty_request_form.html$', 'etc.views.tempredirect', {'path': 'old/request.htm'}),
	)

# URL redirections.
urlpatterns += patterns('django.views.generic.simple',
	url(r'^request$', 'redirect_to', {'url':'/faculty_request_form.html'}),
	url(r'^lending$', 'redirect_to', {'url':'/static/pdf/student_request_form.pdf'}),
	url(r'^equipment$', 'redirect_to', {'url':'/equipment_description.html'}),
	url(r'^policies$', 'redirect_to', {'url':'/lending_policies.html'}),
	url(r'^service$', 'redirect_to', {'url':'/service_request.html'}),
)

# Links to Etcetera.
urlpatterns += patterns('django.views.generic.simple',
		url(r'^service_request.html$', 'redirect_to', {'url': '/etcetera/service/form'}),
)

urlpatterns += patterns('',
	url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'index.html'}),
	url(r'^operating_instructions.html$', 'django.views.generic.simple.direct_to_template', {'template': 'operating_instructions.html'}),
	# The big one.
	url(r'^(?P<path>.*)$', 'etc.views.page'),
)