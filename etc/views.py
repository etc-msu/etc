from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

def page(request, path):
    template_name = ("%s.html" % path, 'base.html')
    return render_to_response(template_name, {}, context_instance=RequestContext(request))

def tempredirect(request, path):
	return redirect("/%s" % path)