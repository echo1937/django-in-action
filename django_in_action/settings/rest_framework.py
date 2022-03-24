REST_FRAMEWORK = {
    # https://www.django-rest-framework.org/api-guide/settings/#default_authentication_classes
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
    ]
}
