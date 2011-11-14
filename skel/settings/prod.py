"""Production settings and globals."""


from os import environ
from sys import exc_info
from urlparse import urlparse, uses_netloc

from S3 import CallingFormat

from common import *


# Helper lambda for gracefully degrading environmental variables:
env = lambda e, d: environ[e] if environ.has_key(e) else d


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-host
EMAIL_HOST = env('EMAIL_HOST', 'smtp.gmail.com')

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', '')

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-host-user
EMAIL_HOST_USER = env('EMAIL_HOST_USER', 'your_email@example.com')

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-port
EMAIL_PORT = env('EMAIL_PORT', 587)

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-use-tls
EMAIL_USE_TLS = True
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
# See: http://devcenter.heroku.com/articles/django#postgres_database_config
uses_netloc.append('postgres')
uses_netloc.append('mysql')

try:
    if environ.has_key('DATABASE_URL'):
        url = urlparse(environ['DATABASE_URL'])
        DATABASES['default'] = {
            'NAME': url.path[1:],
            'USER': url.username,
            'PASSWORD': url.password,
            'HOST': url.hostname,
            'PORT': url.port,
        }
        if url.scheme == 'postgres':
            DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
        if url.scheme == 'mysql':
            DATABASES['default']['ENGINE'] = 'django.db.backends.mysql'
except:
    print "Unexpected error:", exc_info()
########## END DATABASE CONFIGURATION


########## CELERY CONFIGURATION
# See: http://docs.celeryproject.org/en/latest/configuration.html#broker-transport
BROKER_TRANSPORT = 'amqplib'

# See: http://docs.celeryproject.org/en/latest/configuration.html#broker-url
BROKER_URL = env('RABBITMQ_URL', '')

# See: http://docs.celeryproject.org/en/latest/configuration.html#celery-result-backend
CELERY_RESULT_BACKEND = 'amqp'

# See: http://docs.celeryproject.org/en/latest/configuration.html#celery-task-result-expires
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 5
########## END CELERY CONFIGURATION


########## STORAGE CONFIGURATION
# See: http://django-storages.readthedocs.org/en/latest/index.html
INSTALLED_APPS += (
    'storages',
)

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN

AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY', '')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME', '')

STATIC_URL = 'https://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME
########## END STORAGE CONFIGURATION


########## WEBSERVER CONFIGURATION
# See: http://gunicorn.org/
INSTALLED_APPS += (
    'gunicorn',
)
########## END WEBSERVER CONFIGURATION
