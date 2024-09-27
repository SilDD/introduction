from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-e11-2_)rqx#-(x^*62h#(i296q%(xwh(4sz$&2m@822lbvzs7="

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = ALLOWED_HOSTS

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
