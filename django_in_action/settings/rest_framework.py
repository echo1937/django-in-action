REST_FRAMEWORK = {
    # https://www.django-rest-framework.org/api-guide/settings/#default_authentication_classes
    # SessionAuthentication不保留的情况下admin访问正常，但api-auth不正常
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    # https://www.django-rest-framework.org/api-guide/permissions/#setting-the-permission-policy
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    # https://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/#adding-pagination
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 3,

    # https://drf-spectacular.readthedocs.io/en/latest/readme.html#installation
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
