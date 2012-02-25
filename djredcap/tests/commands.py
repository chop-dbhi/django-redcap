import os
import sys
from cStringIO import StringIO
from django.test import TestCase
from django.core.management import call_command

__all__ = ('RedcapTestCase',)

def get_filename(filename):
	from djredcap import tests
	return os.path.join(os.path.dirname(tests.__file__), 'fixtures', filename)

class RedcapTestCase(TestCase):
    def setUp(self):
        self.stdout = sys.stdout

    def cleanUp(self):
        sys.stdout = self.stdout

    def test_csv(self):
        buff = StringIO()
        sys.stdout = buff
        call_command('redcap', 'inspect', get_filename('redcap_inspect.csv'))
        buff.seek(0)
        cmp_file = open(get_filename('redcap_inspect.py'))
        self.assertEqual(buff.read(), cmp_file.read())
