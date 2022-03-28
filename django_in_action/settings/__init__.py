from .rest_framework import *
from .settings import *
from .simplejwt import *
from .spectacular import *

if os.environ.get('PROFILE_TYPE') == 'production':
    from .production import *
elif os.environ.get('PROFILE_TYPE') == 'develop':
    from .develop import *
