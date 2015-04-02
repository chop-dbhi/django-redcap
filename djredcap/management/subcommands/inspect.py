import os
import csv
import json
import keyword
import sys
import re
import inflect
import djconvert
from djredcap import _csv
from django.core.management.base import BaseCommand, CommandError

header_keys = (
    'field_name',
    'form_name',
    'section_name',
    'field_type',
    'field_label',
    'choices',
    'field_note',
    'validation_type',
    'min_value',
    'max_value',
    'is_identifier',
    'branching_logic',
    'required',
    'custom_alignment',
    'question_number'
)

field_types = {
    'date_ymd': 'DateField',
    'number': 'FloatField',
    'integer': 'IntegerField',
    'email': 'EmailField',
    'text': 'CharField',
    'textarea': 'TextField',
    'calc': 'FloatField',
    'radio': 'CharField',
    'select': 'CharField',
    'checkbox': 'CharField',
    'yesno': 'BooleanField',
    'truefalse': 'BooleanField',
}

class Command(BaseCommand):
    help = """Attempts to read a REDCap data dictionary (CSV) and output a
    matching JSON file. Then attempts to read a JSON file and output matching
    Django models. Can take either a REDCap CSV file or a json
    file as input."""
    requires_model_validation = False
    db_module = 'django.db'
    args = 'filename'

    def handle(self, fileName=None, *args, **options):
        if not fileName:
            raise CommandError('Enter a filename')

        fin = open(fileName,'rU')
        dialect = csv.Sniffer().sniff(fin.read(1024))
        fin.seek(0)
	
        
        # Open the file in a normal reader to see if the file is a REDCap data dictionary
        # A REDCap data Dictionary begins with the four necessary columns:
        # Variable/Field Name | Form Name | Field Type | Field Label in any order

        reader = _csv.UnicodeDictReader(fin, fieldnames=header_keys, encoding='latin-1', dialect=dialect)
        header = reader.next()
        
        if header['field_name'] != 'Variable / Field Name' or \
            header['form_name'] != 'Form Name' or \
            header['field_type'] != 'Field Type' or \
            header['field_label'] != 'Field Label':

            sys.stderr.write(fileName + '\n')
            sys.stderr.write(header['field_name'] + header['form_name'] + header['field_type'] + header['field_label'] + '\n')
            sys.stderr.write('Invalid header. File must be a valid REDCap data dictionary.\n')
            sys.stderr.flush() 
            sys.exit(1)
        
        if fileName.find('.json') == -1:
            fileName = djconvert.csv_2_json(self, reader, fileName)
        djconvert.json_2_dj(self, fileName)
