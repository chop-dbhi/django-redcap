import sys
import os
import csv
import json
import re
import math
import djfixture
from optparse import make_option
from djredcap import _csv
from django.core.management.base import BaseCommand, CommandError

__project_name__ = ''

class Command(BaseCommand):
    requires_model_validation = False
    db_module = 'django.db'
    args = 'file', 'jsonfile'
    # Add a command line option -o allowing the user to set a filename for output
    # Path can be relative to the CWD
    option_list = BaseCommand.option_list + (
        make_option('-o', '--output-file', dest='output_filename',
                    help='path to which output file is written'),
    )
    def handle(self, file=None, json_file=None, app_name=None,
               *args, **options):
        help = """Generates a fixture.json file from a redcap data csv and a
        matching JSON file."""
        if not file:
            raise CommandError('Enter a valid CSV file')
        if not json_file:
            raise CommandError('Enter a valid JSON file')
        if not app_name:
            raise CommandError('Enter the name of your django project')

        global __project_name__
        __project_name__ = app_name
        fin = open(file, 'rU')
        header_keys = fin.readline().split(',')
        dialect = csv.Sniffer().sniff(fin.read(1024))
        reader = _csv.UnicodeDictReader(fin, fieldnames=header_keys, encoding='latin-1', dialect=dialect)
        reader.next()

	if not options['output_filename']:
            fout = open(os.path.join(os.getcwd(), 'fixtures.json'), 'w+')
        else:
            fout = open(options['output_filename'], 'w+')
        djfixture.csv_2_fixture(self, fin, reader, json_file, __project_name__,
                                fout)
