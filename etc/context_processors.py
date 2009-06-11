from django.conf import settings
from django.utils.encoding import smart_str
from docutils.core import publish_parts


def restify(request):
    filename = request.path_info.split('.')[0].lstrip('/')
    restify_docs = getattr(settings, 'RESTIFY_DOCS', {})
    docutils_settings = getattr(settings, "RESTRUCTUREDTEXT_FILTER_SETTINGS", {})

    try:
        doc = open("%s%s.rst" % (restify_docs, filename), 'rb')
        content = publish_parts(source=smart_str(doc.read()), writer_name="html4css1", settings_overrides=docutils_settings)
        return {'content': content, 'filename': filename}
    except IOError:
        return {}