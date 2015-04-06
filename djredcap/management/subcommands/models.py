import os
import csv
import json
import keyword
import sys
import re
import inflect
import djconvert
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

    def handle(self, file_name=None, *args, **options):
        if not file_name:
            raise CommandError('Enter a filename')

        fin = open(file_name, 'rU')
        dialect = csv.Sniffer().sniff(fin.read(1024))
        fin.seek(0)
        reader = csv.DictReader(fin, fieldnames=header_keys, dialect=dialect)

        reader.next()
        fileName = djconvert.json_2_dj(self, file_name)
