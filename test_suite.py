import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'

from django.core import management

apps = [
	'test',
]

management.call_command(*apps);
