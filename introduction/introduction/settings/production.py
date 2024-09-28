import os
from .base import *


DEBUG = True

SECRET_KEY = "django-insecure-e11-2_)rqx#-(x^*62h#(i296q%(xwh(4sz$&2m@822lbvzs7="
ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS = [
        "https://johannesklaus.me"
]




try:
    from .local import *
except ImportError:
    pass
