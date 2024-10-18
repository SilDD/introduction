import os
from .base import *
from dotenv import load_dotenv

load_dotenv()


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),  # Hier den korrekten Pfad angeben
    }
}



DEBUG =False

SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = ["johannesklaus.me",
                 "www.johannesklaus.me",]

CSRF_TRUSTED_ORIGINS = [
        "https://johannesklaus.me",
    "https://www.johannesklaus.me"
]




try:
    from .local import *
except ImportError:
    pass
