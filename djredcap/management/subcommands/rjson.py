import os
import csv
import json
import keyword
import sys
import re
import inflect
from optparse import make_option
from djredcap import _csv
from .djconvert import csv_2_json
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


class Command(BaseCommand):
    help = """Attempts to read a REDCap data dictionary (CSV) and output a
    matching JSON file. Then attempts to read a JSON file and output matching
    Django models. Can take either a REDCap CSV file or a json file as
    input."""
    requires_model_validation = False
    db_module = 'django.db'
    args = 'filename'
    # Add a command line option -j allowing the user to set a filename for json.
    # Filename is relative to the current working directory.
    option_list = BaseCommand.option_list + (
        make_option('-o', '--output-file', dest='output_filename',
                    help='Filename to which json is written'),
    )
    def handle(self, file_name=None, *args, **options):
        if not file_name:
            raise CommandError('Enter a filename')
        fin = open(file_name, 'rU')
        dialect = csv.Sniffer().sniff(fin.read(1024))
        fin.seek(0)
        reader = _csv.UnicodeDictReader(fin, fieldnames=header_keys, encoding='latin-1', dialect=dialect)
        header = reader.next()

        if header['field_name'] != 'Variable / Field Name' or \
            header['form_name'] != 'Form Name' or \
            header['field_type'] != 'Field Type' or \
            header['field_label'] != 'Field Label':

            sys.stderr.write(file_name + '\n')
            sys.stderr.write(header['field_name'] + header['form_name'] + header['field_type'] + header['field_label'] + '\n')
            sys.stderr.write('Invalid header. File must be a valid REDCap data dictionary.\n')
            sys.stderr.flush() 
            sys.exit(1)

        file_name = csv_2_json(self, reader, file_name, options['output_filename'])
