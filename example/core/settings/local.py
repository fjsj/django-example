from .base import *
import logging

logging.info("Loading local settings")

SITE_URL = 'http://localhost:8000'

SECRET_KEY = 'tqodk9g3*d2hqwu!v*s-b8oxj_+vs_l+7aq15l0d*m=i^uuosm'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django-example',
        'USER': '',
        'PASSWORD': '',
        'HOST': '', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '', # Set to empty string for default.
    }
}

TEST_DISCOVER_TOP_LEVEL = root()
