from .settings import *

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': './crm_database.db',
    }
}