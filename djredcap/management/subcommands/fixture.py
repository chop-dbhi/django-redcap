#!/usr/bin/python

import sys
import os
import csv
import json
import re
import math
import djfixture
from django.core.management.base import BaseCommand, CommandError

projectName = '';

class Command(BaseCommand):
	requires_model_validation = False;
	db_module = 'django.db'
	args = 'file','jsonfile';

	def handle(self,file=None,jsonFile=None,appName=None, *args, **options):
		if not file:
			raise CommandError('Enter a valid CSV file');
		if not jsonFile:
			raise CommandError('Enter a valid JSON file');
		if not appName:
			raise CommandError('Enter the name of your django project');
	
		global projectName;
		projectName = appName;
		
		fin = open(file);
		header_keys = fin.readline().split(',')
		dialect = csv.Sniffer().sniff(fin.read(1024));
		reader = csv.DictReader(fin,fieldnames=header_keys,dialect=dialect);
		#print 'reader'
		#print reader;
		reader.next();

		fout = open(os.path.join(os.path.dirname(file),'fixtures.json'),'w+');
		djfixture.csv_2_fixture(self,fin,reader,jsonFile,projectName,fout);
