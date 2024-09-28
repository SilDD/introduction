import os
from .base import *


DEBUG = True

SECRET_KEY = "django-insecure-e11-2_)rqx#-(x^*62h#(i296q%(xwh(4sz$&2m@822lbvzs7="
ALLOWED_HOSTS = ["johannesklaus.me"]

CSRF_TRUSTED_ORIGINS = ALLOWED_HOSTS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # Stellen Sie sicher, dass dies mit dem gemounteten Pfad übereinstimmt
    }
}

try:
    from .local import *
except ImportError:
    pass
