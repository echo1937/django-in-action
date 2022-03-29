from .settings import INSTALLED_APPS

INSTALLED_APPS += [
    'dj_rest_auth',
    # 'dj_rest_auth.registration',
]

# If set to None token authentication will be disabled. In this case at least one of REST_SESSION_LOGIN or REST_USE_JWT must be enabled.
REST_AUTH_TOKEN_MODEL = None
REST_SESSION_LOGIN = False
REST_USE_JWT = True
