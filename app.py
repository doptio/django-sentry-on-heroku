'Sanity-preserving wrapper for Sentry WSGI application.'

from sentry.wsgi import application as sentry_app

# This seems to be the easiest way to make Django and Sentry understand that
# cookies are not *fucking* allowed to by unsecured.
from django.conf import settings

settings.SESSION_COOKIE_SECURE = True
settings.CSRF_COOKIE_SECURE = True

hsts_headers = [
    ('Strict-Transport-Security', 'max-age=31536000;'),
]

def application(environ, start_response):
    if environ['HTTP_X_FORWARDED_PROTO'] != 'https':
        location = 'https://%(SERVER_NAME)s' % environ
        start_response('302 Look over there',
                       [('Location', location)])
        return ['Look over there']

    environ['wsgi.url_scheme'] = environ['HTTP_X_FORWARDED_PROTO']

    def sr_wrapper(status, headers, exc_info=None):
        headers_dict = dict((h.lower(), v)
                            for h, v in headers)
        if headers_dict.get('location', '').startswith('http://'):
            raise ValueError('HTTP not allowed')
        headers.extend(hsts_headers)
        return start_response(status, headers, exc_info)

    return sentry_app(environ, sr_wrapper)
