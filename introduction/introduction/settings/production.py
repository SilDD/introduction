import os
from .base import *


DEBUG = False

SECRET_KEY = "django-insecure-e11-2_)rqx#-(x^*62h#(i296q%(xwh(4sz$&2m@822lbvzs7="
ALLOWED_HOSTS = ["johannesklaus.me"]

CSRF_TRUSTED_ORIGINS = ALLOWED_HOSTS
ROOT_URLCONF = "introduction.urls"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),  # Stelle sicher, dass der Pfad korrekt ist
    }
}


try:
    from .local import *
except ImportError:
    pass
