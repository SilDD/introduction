DEBUG = True

ALLOWED_HOSTS = ['www.johannesklaus.me', 'johannesklaus.me']

try:
    from .local import *
except ImportError:
    pass
