import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(__file__), 'tests.db'),
    }
}

ROOT_URLCONF = '';

INSTALLED_APPS = (
    #'django.contrib.sites',
    #'django.contrib.auth',
    #'django.contrib.contenttypes',

    'djredcap',
)

SITE_ID = 1;
