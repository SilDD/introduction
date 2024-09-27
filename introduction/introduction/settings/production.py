from .base import *
from .dev import ALLOWED_HOSTS

DEBUG = False

ALLOWED_HOSTS = ['www.johannesklaus.me', 'johannesklaus.me']

try:
    from .local import *
except ImportError:
    pass
