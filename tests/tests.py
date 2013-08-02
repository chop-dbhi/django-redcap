import os
import sys
import shutil
from cStringIO import StringIO
from django.test import TestCase
from django.core.management import call_command
from itertools import izip
from itertools import izip_longest

__all__ = ('RedcapTestCase','FixtureTestCase','ModelsTestCase','JsonTestCase','ConvertTestCase')
def get_filename(filename):
    return os.path.join(os.path.dirname(__file__), 'fixtures', filename)


def split_assert(self, line1, line2):
    data1 = line1.rstrip('\n').replace(" ","").replace(",","").split(':')
    data2 = line2.rstrip('\n').replace(" ","").replace(",","").split(':') 
    
    try:
        self.assertEqual(line1, line2)
    except AssertionError:
        self.assertEqual(data1[0], data2[0])
        try:
            self.assertAlmostEqual(float(data1[1]), float(data2[1]))
        except IndexError:
            pass

class ConvertTestCase(TestCase):
    def test_multi_form_csv_with_repeating_fields(self):
        fileName = 'multi_form_with_rep_fields'
        csv_fileName = fileName + '.csv'
        json_fileName = fileName + '.json'
        shutil.copy(get_filename(json_fileName),get_filename(json_fileName + '2'))
        cmp_fileName = 'cmp_' + fileName + '.py'      
        call_command('redcap','convert',get_filename(csv_fileName))
        cmp_file = open(get_filename(cmp_fileName))
        for line1, line2 in izip(open(get_filename('models.py'),'r'),open(get_filename(cmp_fileName),'r')):
            self.assertEqual(line1,line2)   

    def test_single_form_csv_with_rep_fields_start_with_repeat(self):
        fileName = 'single_form_with_rep_fields_start_with_repeat'
        csv_fileName = fileName + '.csv'
        json_fileName = fileName + '.json'
        shutil.copy(get_filename(json_fileName),get_filename(json_fileName + '2'))
        cmp_fileName = 'cmp_' + fileName + '.py'
        call_command('redcap','convert',get_filename(csv_fileName))
        cmp_file = open(get_filename('cmp_' + fileName + '.py'))
        for line1, line2 in izip(open(get_filename('models.py'),'r'),open(get_filename(cmp_fileName),'r')):
            self.assertEqual(line1,line2)
        shutil.copy(get_filename(json_fileName + '2'),get_filename(json_fileName))
                

    def test_single_form_csv_with_rep_fields_many_nested(self):
        fileName = 'single_form_with_rep_fields_many_nested'
        csv_fileName = fileName + '.csv'
        json_fileName = fileName + '.json'
        shutil.copy(get_filename(json_fileName),get_filename(json_fileName + '2'))
        cmp_fileName = 'cmp_' + fileName + '.py'        
        call_command('redcap','convert',get_filename(csv_fileName))
        cmp_file = open(get_filename('cmp_' + fileName + '.py'))
        for line1, line2 in izip(open(get_filename('models.py'),'r'),open(get_filename(cmp_fileName),'r')):
            self.assertEqual(line1,line2)
        shutil.copy(get_filename(json_fileName + '2'),get_filename(json_fileName))


    def test_multi_form_csv_without_repeats(self):
        fileName = 'multi_form_without_rep_fields'
        csv_fileName = fileName + '.csv'
        json_fileName = fileName + '.json'
        shutil.copy(get_filename(json_fileName),get_filename(json_fileName + '2'))
        cmp_fileName = 'cmp_' + fileName + '.py'        
        call_command('redcap','convert',get_filename(csv_fileName))
        cmp_file = open(get_filename('cmp_' + fileName + '.py'))
        for line1, line2 in izip(open(get_filename('models.py'),'r'),open(get_filename(cmp_fileName),'r')):
            self.assertEqual(line1,line2)
        shutil.copy(get_filename(json_fileName + '2'),get_filename(json_fileName))

    
    def test_single_form_csv_without_repeats(self):
        fileName = 'single_form_without_rep_fields'
        csv_fileName = fileName + '.csv'
        json_fileName = fileName + '.json'
        shutil.copy(get_filename(json_fileName),get_filename(json_fileName + '2'))
        cmp_fileName = 'cmp_' + fileName + '.py'        
        call_command('redcap','convert',get_filename(csv_fileName))
        cmp_file = open(get_filename('cmp_' + fileName + '.py'))
        for line1, line2 in izip(open(get_filename('models.py'),'r'),open(get_filename(cmp_fileName),'r')):
            self.assertEqual(line1,line2)
        shutil.copy(get_filename(json_fileName + '2'),get_filename(json_fileName))


class JsonTestCase(TestCase):
    def test_multi_form_csv_with_repeating_fields(self):
        fileName = 'multi_form_with_rep_fields'
        csv_fileName = fileName + '.csv'
        cmp_fileName = 'cmp_' + fileName + '.json'      
        call_command('redcap','json',get_filename(csv_fileName))
        cmp_file = open(get_filename(cmp_fileName))
        for line1, line2 in izip(open(get_filename(fileName + '.json'),'r'),open(get_filename(cmp_fileName),'r')):
            self.assertEqual(line1,line2)   

    def test_single_form_csv_with_rep_fields_start_with_repeat(self):
        fileName = 'single_form_with_rep_fields_start_with_repeat'
        csv_fileName = fileName + '.csv'
        cmp_fileName = 'cmp_' + fileName + '.json'
        call_command('redcap','json',get_filename(csv_fileName))
        cmp_file = open(get_filename('cmp_' + fileName + '.py'))
        for line1, line2 in izip(open(get_filename(fileName + '.json'),'r'),open(get_filename(cmp_fileName),'r')):
            self.assertEqual(line1,line2)
    def test_single_form_csv_with_rep_fields_many_nested(self):
        fileName = 'single_form_with_rep_fields_many_nested'
        csv_fileName = fileName + '.csv'
        cmp_fileName = 'cmp_' + fileName + '.json'        
        call_command('redcap','json',get_filename(csv_fileName))
        cmp_file = open(get_filename('cmp_' + fileName + '.py'))
        for line1, line2 in izip(open(get_filename(fileName + '.json'),'r'),open(get_filename(cmp_fileName),'r')):
            self.assertEqual(line1,line2)

    def test_multi_form_csv_without_repeats(self):
        fileName = 'multi_form_without_rep_fields'
        csv_fileName = fileName + '.csv'
        cmp_fileName = 'cmp_' + fileName + '.json'        
        call_command('redcap','json',get_filename(csv_fileName))
        cmp_file = open(get_filename('cmp_' + fileName + '.py'))
        for line1, line2 in izip(open(get_filename(fileName + '.json'),'r'),open(get_filename(cmp_fileName),'r')):
            self.assertEqual(line1,line2)
    
    def test_single_form_csv_without_repeats(self):
        fileName = 'single_form_without_rep_fields'
        csv_fileName = fileName + '.csv'
        cmp_fileName = 'cmp_' + fileName + '.json'        
        call_command('redcap','json',get_filename(csv_fileName))
        cmp_file = open(get_filename('cmp_' + fileName + '.py'))
        for line1, line2 in izip(open(get_filename(fileName + '.json'),'r'),open(get_filename(cmp_fileName),'r')):
            self.assertEqual(line1,line2)


class ModelsTestCase(TestCase):
    def test_multi_form_csv_with_repeating_fields(self):
        fileName = 'multi_form_with_rep_fields'
        csv_fileName = fileName + '.json'
        cmp_fileName = 'cmp_' + fileName + '.py'      
        call_command('redcap','models',get_filename(csv_fileName))
        cmp_file = open(get_filename(cmp_fileName))
        for line1, line2 in izip(open(get_filename('models.py'),'r'),open(get_filename(cmp_fileName),'r')):
            self.assertEqual(line1,line2)   

    def test_single_form_csv_with_rep_fields_start_with_repeat(self):
        fileName = 'single_form_with_rep_fields_start_with_repeat'
        csv_fileName = fileName + '.json'
        cmp_fileName = 'cmp_' + fileName + '.py'
        call_command('redcap','models',get_filename(csv_fileName))
        cmp_file = open(get_filename('cmp_' + fileName + '.py'))
        for line1, line2 in izip(open(get_filename('models.py'),'r'),open(get_filename(cmp_fileName),'r')):
            self.assertEqual(line1,line2)
    
    def test_single_form_csv_with_rep_fields_many_nested(self):
        fileName = 'single_form_with_rep_fields_many_nested'
        csv_fileName = fileName + '.json'
        cmp_fileName = 'cmp_' + fileName + '.py'        
        call_command('redcap','models',get_filename(csv_fileName))
        cmp_file = open(get_filename('cmp_' + fileName + '.py'))
        for line1, line2 in izip(open(get_filename('models.py'),'r'),open(get_filename(cmp_fileName),'r')):
            self.assertEqual(line1,line2)

    def test_multi_form_csv_without_repeats(self):
        fileName = 'multi_form_without_rep_fields'
        csv_fileName = fileName + '.json'
        cmp_fileName = 'cmp_' + fileName + '.py'        
        call_command('redcap','models',get_filename(csv_fileName))
        cmp_file = open(get_filename('cmp_' + fileName + '.py'))
        for line1, line2 in izip(open(get_filename('models.py'),'r'),open(get_filename(cmp_fileName),'r')):
            self.assertEqual(line1,line2)
    
    def test_single_form_csv_without_repeats(self):
        fileName = 'single_form_without_rep_fields'
        csv_fileName = fileName + '.json'
        cmp_fileName = 'cmp_' + fileName + '.py'        
        call_command('redcap','models',get_filename(csv_fileName))
        cmp_file = open(get_filename('cmp_' + fileName + '.py'))
        for line1, line2 in izip(open(get_filename('models.py'),'r'),open(get_filename(cmp_fileName),'r')):
            self.assertEqual(line1,line2)
    

class FixtureTestCase(TestCase):
    def test_csv_with_repeating_fields(self):
        file_name = 'fixture_with_rep_fields'
        csv_file_name1 = file_name + '.csv'
        csv_file_name2 = file_name + '.json'
        cmp_file_name = 'cmp_' + file_name + '.json'
        call_command('redcap','fixture',get_filename(csv_file_name1),
                    get_filename(csv_file_name2),'mysite')
        cmp_file = open(get_filename(cmp_file_name))
        for line1, line2 in izip(open(get_filename('fixtures.json'),'r'),
                                    open(get_filename(cmp_file_name),'r')):
            split_assert(self, line1, line2)

    def test_csv_without_repeating_fields(self):
        file_name = 'fixture_without_rep_fields'
        csv_file_name1 = file_name + '.csv'
        csv_file_name2 = file_name + '.json'
        cmp_file_name = 'cmp_' + file_name + '.json'
        call_command('redcap','fixture',get_filename(csv_file_name1),              
                                    get_filename(csv_file_name2),'mysite')
        cmp_file = open(get_filename(cmp_file_name))
        for line1, line2 in izip(open(get_filename('fixtures.json'),'r'),
                                    open(get_filename(cmp_file_name),'r')):
            split_assert(self,line1,line2)


class RedcapTestCase(TestCase):
    def test_multi_form_csv_with_repeating_fields(self):
        fileName = 'multi_form_with_rep_fields'
        csv_fileName = fileName + '.csv'
        cmp_fileName = 'cmp_' + fileName + '.py'      
        call_command('redcap','inspect',get_filename(csv_fileName))
        cmp_file = open(get_filename(cmp_fileName))
        for line1, line2 in izip(open(get_filename('models.py'),'r'),open(get_filename(cmp_fileName),'r')):
            self.assertEqual(line1,line2)   

    def test_single_form_csv_with_rep_fields_start_with_repeat(self):
        fileName = 'single_form_with_rep_fields_start_with_repeat'
        csv_fileName = fileName + '.csv'
        cmp_fileName = 'cmp_' + fileName + '.py'
        call_command('redcap','inspect',get_filename(csv_fileName))
        cmp_file = open(get_filename('cmp_' + fileName + '.py'))
        for line1, line2 in izip(open(get_filename('models.py'),'r'),open(get_filename(cmp_fileName),'r')):
            self.assertEqual(line1,line2)
    def test_single_form_csv_with_rep_fields_many_nested(self):
        fileName = 'single_form_with_rep_fields_many_nested'
        csv_fileName = fileName + '.csv'
        cmp_fileName = 'cmp_' + fileName + '.py'        
        call_command('redcap','inspect',get_filename(csv_fileName))
        cmp_file = open(get_filename('cmp_' + fileName + '.py'))
        for line1, line2 in izip(open(get_filename('models.py'),'r'),open(get_filename(cmp_fileName),'r')):
            self.assertEqual(line1,line2)

    def test_multi_form_csv_without_repeats(self):
        fileName = 'multi_form_without_rep_fields'
        csv_fileName = fileName + '.csv'
        cmp_fileName = 'cmp_' + fileName + '.py'        
        call_command('redcap','inspect',get_filename(csv_fileName))
        cmp_file = open(get_filename('cmp_' + fileName + '.py'))
        for line1, line2 in izip(open(get_filename('models.py'),'r'),open(get_filename(cmp_fileName),'r')):
            self.assertEqual(line1,line2)
    
    def test_single_form_csv_without_repeats(self):
        fileName = 'single_form_without_rep_fields'
        csv_fileName = fileName + '.csv'
        cmp_fileName = 'cmp_' + fileName + '.py'        
        call_command('redcap','inspect',get_filename(csv_fileName))
        cmp_file = open(get_filename('cmp_' + fileName + '.py'))
        for line1, line2 in izip(open(get_filename('models.py'),'r'),open(get_filename(cmp_fileName),'r')):
            self.assertEqual(line1,line2)
