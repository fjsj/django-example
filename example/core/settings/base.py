#coding=utf-8

import os
from os.path import join, abspath, dirname
from sys import path
import logging
from django.conf import global_settings as DEFAULT_SETTINGS

from django.core.exceptions import ImproperlyConfigured

def get_env_variable(var_name):
    try:
        var = os.environ.get(var_name)
        if not var:
            raise Exception
        return var
    except:
        error_msg = "Set the %s environment variable" % var_name
        logging.error(error_msg)
        raise ImproperlyConfigured(error_msg)

# Path tools
here = lambda *x: join(abspath(dirname(__file__)), *x)
PROJECT_ROOT = here("..", "..")
root = lambda *x: join(abspath(PROJECT_ROOT), *x)

path.append(PROJECT_ROOT)
# End path tools

MEDIA_ROOT = root('../uploads')
MEDIA_URL = '/uploads/'

STATIC_ROOT = root('../static')
STATIC_URL = '/static/'

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Admin', 'flavio+example@vinta.com.br'),
)
MANAGERS = ADMINS

EMAIL_FROM = 'flavio+example@vinta.com.br'

ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'America/Recife'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-US'

LANGUAGES = (
    ('en-US', 'English (US)'),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

USE_TZ = True

STATICFILES_DIRS = (

)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_DIRS = (

)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    'url_tools.context_processors.current_url',
    'core.context_processors.site_url',
    'core.context_processors.view_name',
)

JS_CONTEXT_ENABLED = False

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.messages',
    'precompressed',  # must be before staticfiles
    'django.contrib.staticfiles',
    'django.contrib.admin',

    'djangojs',
    'south',
    'url_tools',

    'core',
    'notes',
)

STATICFILES_STORAGE = 'precompressed.storage.PrecompressedStaticFilesStorage'

def get_gzipped_name(name):
    """
    returns the location of the gzipped version of a specified file.
    changed to be compatible with nginx gzip_static module (file name ends with .gz)
    """
    file_ext_index = name.rfind('.')
    file_name, file_ext = name[:file_ext_index], name[file_ext_index:]
    return '%s%s.gz' % (file_name, file_ext)

PRECOMPRESSED_SETTINGS = {
    'get_gzipped_name': get_gzipped_name
}


from django.core.exceptions import SuspiciousOperation
def skip_suspicious_operations(record):
    if record.exc_info:
        exc_value = record.exc_info[1]
        if isinstance(exc_value, SuspiciousOperation):
            return False
        return True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'skip_suspicious_operations': {
            '()': 'django.utils.log.CallbackFilter',
            'callback': skip_suspicious_operations,
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false', 'skip_suspicious_operations'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
