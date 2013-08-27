import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(__file__), 'tests.db'),
    }
}

INSTALLED_APPS = (
    'djredcap',
    'tests',
)

SECRET_KEY = 'xSECRETx'
