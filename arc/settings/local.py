from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR , 'db.sqlite3'),
    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child("static")]
STATIC_ROOT = BASE_DIR.child('staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')
AUTH_USER_MODEL = 'users.User'