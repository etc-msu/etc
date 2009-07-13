from django.shortcuts import render_to_response
from django.template import RequestContext
from etc.user_forms import forms as user_forms

def page(request, path):
    template_name = ("%s.html" % path, 'base.html')
    return render_to_response(template_name, {}, context_instance=RequestContext(request))

def service(request):
	form = user_forms.ServiceForm()
	context = {'form':form,}
	return render_to_response("form.html", context, context_instance=RequestContext(request))