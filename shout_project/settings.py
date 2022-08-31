"""
Django settings for shout_project project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(1o-psk&4db39^@ae8d@3!#$5hd!my#&o%@x1!%-&-#rx&2tb^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['5ac2-171-99-160-24.ngrok.io', '127.0.0.1', 'localhost']

TEMP_HOST = 'https://5ac2-171-99-160-24.ngrok.io/'
LINE_CLIENT_ID = '1656634729'
LINE_CLIENT_SECRET = 'a9123c0aeec0fb3e37fbed8391411930'
FB_CLIENT_ID = '3117293068558780'
FB_CLIENT_SECRET = '9d42ea694e12400f87c6262dd9c60a6a'

LINE_CHANNEL_ACCESS_TOKEN = '2vlk1sbdeB/YgPsZlUzFxq647gDOeVBhs+swmUG1XOGFol9YCN48D9I+XD/6gBXqi1j+aSwUcwTS42j1XcDgb2nK0OofFGPyjqHtrC+a/qD0nadY3KGqnvOMBgiEE0Aku/l19AcDAQYgO3V2WnLMZAdB04t89/1O/w1cDnyilFU='


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',    
    'accounts',
    'api',
    'brands',
    'campaigns',
    'orders',
    'pages',
    'selections',
    'shouters',
    'rest_framework',
    'rest_framework_simplejwt',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shout_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'shout_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'shout_test',
        'USERNAME': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': 5433
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME':  BASE_DIR / 'db.sqlite3'
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Bangkok'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#
# try:
#     from .local_settings import *
# except ImportError:
#     pass


# # Email Verification
# def verified_callback(user):
#     user.is_active = True
#
# EMAIL_VERIFIED_CALLBACK = verified_callback
# EMAIL_FROM_ADDRESS = 'noreply@aliasaddress.com'
# EMAIL_MAIL_SUBJECT = 'Confirm your email'
# EMAIL_MAIL_HTML = 'mail_body.html'
# EMAIL_MAIL_PLAIN = 'mail_body.txt'
# EMAIL_TOKEN_LIFE = 60 * 60
# EMAIL_PAGE_TEMPLATE = 'confirm_template.html'
# EMAIL_PAGE_DOMAIN = 'http://www.shoutsolution.com/'
# EMAIL_MULTI_USER = True  # optional (defaults to False)
#
# For Django Email Backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'noreply@shoutsolution.com'
EMAIL_HOST_PASSWORD = 'ytubfpbfqmqrvuzh'  # os.environ['password_key'] suggested
EMAIL_USE_TLS = True
