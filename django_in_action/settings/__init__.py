import os
from .settings import *
from .rest_framework import *

if os.environ.get('PROFILE_TYPE') == 'production':
    from .production import *
elif os.environ.get('PROFILE_TYPE') == 'develop':
    from .develop import *
