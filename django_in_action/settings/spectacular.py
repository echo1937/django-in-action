from .settings import INSTALLED_APPS

INSTALLED_APPS += [
    'drf_spectacular',
    'drf_spectacular_sidecar',
]

SPECTACULAR_SETTINGS = {
    'TITLE': 'Django-In-Action APIs',
    'DESCRIPTION': 'Sane and flexible OpenAPI 3 schema generation for Django REST framework.',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
    'SWAGGER_UI_DIST': 'SIDECAR',  # shorthand to use the sidecar instead
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
}
