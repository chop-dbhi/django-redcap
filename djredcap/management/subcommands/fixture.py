#!/usr/bin/python

import sys
import os
import csv
import json
import re
import math
import djfixture
from django.core.management.base import BaseCommand, CommandError

__project_name__ = ''


class Command(BaseCommand):
    requires_model_validation = False
    db_module = 'django.db'
    args = 'file', 'jsonfile'

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
        fin = open(file)
        header_keys = fin.readline().split(',')
        dialect = csv.Sniffer().sniff(fin.read(1024))
        reader = csv.DictReader(fin, fieldnames=header_keys, dialect=dialect)
        reader.next()

        fout = open(os.path.join(os.path.dirname(file), 'fixtures.json'), 'w+')
        djfixture.csv_2_fixture(self, fin, reader, json_file, __project_name__,
                                fout)
