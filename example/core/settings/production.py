from .base import *
import logging

logging.info("Loading local settings")

SITE_URL = 'http://www.example.com'

SECRET_KEY = 'x%m3f&xlp33%*@97m%i74q9+wzu8e+0bl8^2+rald#%ao+u5fm'

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django-example',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '', # Set to empty string for default.
    }
}

ALLOWED_HOSTS = ['*']
