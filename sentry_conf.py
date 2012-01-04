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
SENTRY_KEY = os.environ['SENTRY_KEY']
