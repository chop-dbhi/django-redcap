#!/usr/bin/python

import os
import csv
import json
import keyword
import sys
import re
import inflect
from optparse import make_option
import djredcap
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
    help = """Attempts to read a REDCap data dictionary (CSV) and generates a
    matching JSON file. Then attempts to read a generated  JSON file and output
    matching Django models. Takes a redcap CSV as input. Skips outputting JSON
    file unless option --JSON is used."""

    requires_model_validation = False
    db_module = 'django.db'
    args = 'filename'

    json_filename = ''

    option_list = BaseCommand.option_list + (
        make_option('--JSON', action='store', dest='json',
                    help='Print a JSON file when using convert, default no'),
    )

    def handle(self, file_name=None, *args, **options):
        if not file_name:
            raise CommandError('Enter a filename')

        json_filename = options.get('json')
        fin = open(file_name)
        dialect = csv.Sniffer().sniff(fin.read(1024))
        fin.seek(0)
        reader = csv.DictReader(fin, fieldnames=header_keys, dialect=dialect)

        reader.next()

        file_name = djredcap.csv2json(self, reader, file_name)
        file_name1 = file_name
        djredcap.json2dj(self, file_name)
        if json_filename:
            os.rename(file_name1, json_filename)
        else:
            os.remove(os.path.join(os.path.dirname(file_name1), file_name1))
