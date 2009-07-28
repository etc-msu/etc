import os

DEBUG = True
DATABASE_ENGINE = 'postgresql_psycopg2'
DATABASE_NAME = 'etcetera'
DATABASE_USER = 'etcetera'
DATABASE_PASSWORD = 'etcetera'
DATABASE_HOST = 'localhost'
DATABASE_PORT = ''
ROOT_URLCONF = 'etc.urls'
PROJECT_DIR = os.path.dirname(__file__)
TEMPLATE_DIRS = (PROJECT_DIR + '/templates/',)
RESTRUCTUREDTEXT_FILTER_SETTINGS = {'cloak_email_addresses': True}
TEMPLATE_CONTEXT_PROCESSORS = ('etc.context_processors.restify',)
RESTIFY_DOCS = PROJECT_DIR + '/docs/'
INSTALLED_APPS = (
	'etc.user_forms',
	'etc.structure',
)