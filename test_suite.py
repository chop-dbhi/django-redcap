import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'djredcap.tests.settings'

from django.core import management

apps = [
	'test',
]

management.call_command(*apps);
