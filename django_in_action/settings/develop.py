from .settings import INSTALLED_APPS

INSTALLED_APPS += [
    # 'quickstart',
    'snippets',
]
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_in_action',
        'USER': 'root',
        'PASSWORD': 'redhat',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
