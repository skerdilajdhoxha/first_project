from .base import *


try:
    from .local import *
except:
    pass


try:
    from .production import *
except ImportError:
    print ".production doesn't exist"

