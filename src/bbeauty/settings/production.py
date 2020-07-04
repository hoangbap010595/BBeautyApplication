from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['bbeauty.vn', ]


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'BBeautyStorage',
        'USER': 'postgres',
        'PASSWORD': 'Hoang911',
        'HOST': '139.180.188.85',
        'PORT': '5432',
    },
    'payment': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'BBeautyPayment',
        'USER': 'postgres',
        'PASSWORD': 'Hoang911',
        'HOST': '139.180.188.85',
        'PORT': '5432',
    }
}



CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '139.180.188.85:11211',
    }
}