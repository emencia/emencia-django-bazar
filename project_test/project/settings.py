"""
Django settings for sample project.

Generated by 'django-admin startproject' using Django 1.8.13.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lz20$v9%=fd-hu$m!)_uc=0t)2cnks_jbx(8x(1_7j&j7y-d+4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'autobreadcrumbs',
    'localflavor',
    'taggit',
    'taggit_templatetags2',
    'djangocodemirror',
    'sendfile',
    'bazar',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'



"""
NOTE:
    * Every things above comes from default generated settings file (from Django startproject);
    * Every things below are needed settings for Bazar and its third apps;
    * Don't edit default generated settings, instead edit them again below;
"""
PROJECT_PATH = os.path.join(BASE_DIR, 'project')

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')

TEMPLATES[0]['DIRS'] = (os.path.join(PROJECT_PATH, "templates"),)

#
# Default Bazar settings
#
from bazar.settings import *

# Backend type: do not define any other backend that the development one, for
# other environnement define backend in their own setting file
SENDFILE_BACKEND = 'sendfile.backends.development' # Dummy backend for django's wsgi 'runserver'
#SENDFILE_BACKEND = 'sendfile.backends.nginx' # For Nginx
#SENDFILE_BACKEND = 'sendfile.backends.xsendfile' # For Apache or Lighttpd

#
# Settings for sendfile requirement
#
# Protected files directory name, this dir have to exists in your project, but don't put
# it under media or static dir as it will be served unprotected
PROTECTED_MEDIAS_DIRNAME = 'protected_medias'

# Send File paths and url
SENDFILE_ROOT = os.path.join(PROJECT_PATH, PROTECTED_MEDIAS_DIRNAME)
SENDFILE_URL = '/%s' % PROTECTED_MEDIAS_DIRNAME
