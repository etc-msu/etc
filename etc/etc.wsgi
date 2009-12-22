import os
import sys
import site

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
SUB_SITE_ROOT = os.path.dirname(SITE_ROOT)
VIRTUALENV_ROOT = os.path.dirname(SUB_SITE_ROOT)
SITE_PACKAGES_DIR = os.path.join(
	VIRTUALENV_ROOT,
	'lib/python2.6/site-packages'
)
sys.path.append(SITE_ROOT)
sys.path.append(SUB_SITE_ROOT)
sys.path.append(VIRTUALENV_ROOT)
sys.path.append(SITE_PACKAGES_DIR)
site.addsitedir(SITE_PACKAGES_DIR)

os.environ['DJANGO_SETTINGS_MODULE'] = 'etc.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
