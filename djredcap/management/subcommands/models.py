import os
import csv
import json
import keyword
import sys
import re
import inflect
import djconvert
from optparse import make_option
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
    help = """Attempts to generate a models.py from a matching JSON file."""
    requires_model_validation = False
    db_module = 'django.db'
    args = 'filename'
    # Add a command line option -m allowing the user to set a filename for models.
    # Filename is relative to the current working directory.
    option_list = BaseCommand.option_list + (
        make_option('-o', '--output-file', dest='output_filename',
                    help='Filename to which models are written'),
    )

    def handle(self, file_name=None, *args, **options):
        if not file_name:
            raise CommandError('Enter a filename')

        fin = open(file_name, 'rU')
        dialect = csv.Sniffer().sniff(fin.read(1024))
        fin.seek(0)
        reader = csv.DictReader(fin, fieldnames=header_keys, dialect=dialect)

        reader.next()
        fileName = djconvert.json_2_dj(self, file_name, options['output_filename'])
