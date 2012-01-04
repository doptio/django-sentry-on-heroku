#!/usr/bin/env python

from sentry.conf.server import *

import os
from urlparse import urlparse

database_url = os.environ.get('DATABASE_URL',
                              'postgres://sentry:sentry@localhost/sentry')
db = urlparse(database_url)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': db.path[1:],
        'USER': db.username,
        'PASSWORD': db.password,
        'HOST': db.hostname,
        'PORT': db.port,
    }
}

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = int(os.environ.get('PORT', 9000))

SENTRY_PUBLIC = False
SENTRY_KEY = os.environ.get('SENTRY_KEY')

if 'MAIL_TO' in os.environ:
    ADMINS = [('J. Doe', os.environ['MAIL_TO'])]
    SENTRY_ADMINS = [os.environ['MAIL_TO']]

SERVER_EMAIL = os.environ.get('SENDGRID_USERNAME')

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME')
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
