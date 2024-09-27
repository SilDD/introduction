from .base import *
from .dev import ALLOWED_HOSTS

DEBUG = True

ALLOWED_HOSTS = ["*"]

try:
    from .local import *
except ImportError:
    pass
