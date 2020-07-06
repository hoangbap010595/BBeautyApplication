from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


INSTALLED_APPS += [
    'rest_framework',
    'apps.account',
    'apps.system',
]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'BBeautyStorage',
        'USER': 'postgres',
        'PASSWORD': 'Hoang911',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
    'payment': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'BBeautyPayment',
        'USER': 'postgres',
        'PASSWORD': 'Hoang911',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 25
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')


LOGIN_REDIRECT_URL = '/account/profile/'
LOGOUT_REDIRECT_URL = '/account/login/'
LOGIN_URL = '/account/login/'

# APPLICATION CONFIG
BBEAUTY_PAGGING_LENGTH = 2