import os
import sys
from cStringIO import StringIO
from django.test import TestCase
from django.core.management import call_command
from itertools import izip
from itertools import izip_longest

__all__ = ('RedcapTestCase',)
def get_filename(filename):
	from djredcap import tests
	return os.path.join(os.path.dirname(tests.__file__), 'fixtures', filename)

#def assert_files(file1, file2):
	#for line1, line2 in izip_longest(open(file1,'r'),open(file2,'r')):
	#	assertEqual(line1,line2);

class RedcapTestCase(TestCase):
    def test_multiple_form_csv_with_repeating_fields(self):
        fileName = 'multi_form_with_rep_fields';
        csv_fileName = fileName + '.csv';
        cmp_fileName = 'cmp_' + fileName + '.py';      
	call_command('redcap','inspect',get_filename(csv_fileName));
        cmp_file = open(get_filename(cmp_fileName));
	for line1, line2 in izip(open(get_filename(fileName + '.py'),'r'),open(get_filename(cmp_fileName),'r')):
		self.assertEqual(line1,line2);	

    def	test_single_form_csv_with_rep_fields_start_with_repeat(self):
	fileName = 'single_form_with_rep_fields_start_with_repeat';
	csv_fileName = fileName + '.csv';
	cmp_fileName = 'cmp_' + fileName + '.py';
	call_command('redcap','inspect',get_filename(csv_fileName));
	cmp_file = open(get_filename('cmp_' + fileName + '.py'));
	for line1, line2 in izip(open(get_filename(fileName + '.py'),'r'),open(get_filename(cmp_fileName),'r')):
                self.assertEqual(line1,line2);
    def test_single_form_csv_with_rep_fields_many_nested(self):
        fileName = 'single_form_with_rep_fields_many_nested';
        csv_fileName = fileName + '.csv';
        cmp_fileName = 'cmp_' + fileName + '.py';        
	call_command('redcap','inspect',get_filename(csv_fileName));
        cmp_file = open(get_filename('cmp_' + fileName + '.py'));
        for line1, line2 in izip(open(get_filename(fileName + '.py'),'r'),open(get_filename(cmp_fileName),'r')):
                self.assertEqual(line1,line2);

    def test_multiple_form_csv_without_repeats(self):
        fileName = 'multi_form_without_rep_fields';
        csv_fileName = fileName + '.csv';
        cmp_fileName = 'cmp_' + fileName + '.py';        
	call_command('redcap','inspect',get_filename(csv_fileName));
        cmp_file = open(get_filename('cmp_' + fileName + '.py'));
        for line1, line2 in izip(open(get_filename(fileName + '.py'),'r'),open(get_filename(cmp_fileName),'r')):
                self.assertEqual(line1,line2);
	
    def test_single_form_csv_without_repeats(self):
        fileName = 'single_form_without_rep_fields';
        csv_fileName = fileName + '.csv';
        cmp_fileName = 'cmp_' + fileName + '.py';        
	call_command('redcap','inspect',get_filename(csv_fileName));
        cmp_file = open(get_filename('cmp_' + fileName + '.py'));
        for line1, line2 in izip(open(get_filename(fileName + '.py'),'r'),open(get_filename(cmp_fileName),'r')):
                self.assertEqual(line1,line2);
