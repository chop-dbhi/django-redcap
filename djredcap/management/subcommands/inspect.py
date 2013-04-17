import csv
import json
import keyword
import sys
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
	help = """Attempts to read a REDCap data dictionary (CSV) and output a matching JSON file.
	Then attempts to read a JSON file and output matching Django models. Can take either a REDCap
	CSV file or a json file as input."""
	requires_model_validation = False;
	db_module = 'django.db'
	args = 'filename';

	def readFile(self, fileName=None):
		if not fileName:
			fileName = raw_input('Enter a valid filename: ');
	
		fin = open(fileName);
		dialect = csv.Sniffer().sniff(fin.read(1024));
		fin.seek(0);
		reader = csv.DictReader(fin, fieldnames=header_keys,dialect=dialect);
	
		reader.next();
		if fileName.find('.json') == -1:
			fileName = csv2json(reader, fileName);
		json2dj(fileName);

	def csv2json(self, reader, fileName):
		"""
		Function that converts csv file to valid json. 
		"""
		fout = open(fileName + '.json', "w+");
		
		repeat_rows_list = [];
		all_repeats = [];
		form_list = [''];
		last_form_name = None;
		cur_depth = 0;
		for row in reader:
			"""
			Printing the list of repeating rows built below.
			"""
			if row['form_name']:
				form_list[0] = row['form_name'];
				if row['form_name'] != last_form_name:
					if last_form_name:
						print_list(all_repeats,fout);
						all_repeats = [];
					last_form_name = row['form_name'];
			"""
			Needed for special case csv's with repeats used, not needed otherwise.
			An array of rows is built depending on if that row has a startrepeat, endrepeat, or
			repeat in it. Every row between a startrepeat and endrepeat is added to the 
			array, while keeping track of the current depth of the array.
	
			An array might look like: [[-,-,-,[-,[-,-,-],-,[-,-,]]]], where each - is a 
			row and each list, besides the outermost one, is a group of rows inside a 
			startrepeat/endrepeat segment.
	
			The list is then scrubbed of empty indexs and rows with only endrepeat in the 
			field name. Relationships between forms (used for creating foreign keys) are
			made by appending the referenced form to the end of the field_name. 
			"""
			if row['field_name'].find('startrepeat') != -1:
				repeat_info = row['field_name'].strip().split();
				row['field_name'] = repeat_info[0];
				form_list.append(''.join(repeat_info[3:]));
			
				repeat_rows_list = last_inner_append(repeat_rows_list, [row],0,cur_depth);
				cur_depth = cur_depth + 1;
			elif row['field_name'].find('endrepeat') != -1:
				row['field_name'] = row['field_name'].strip().split()[0];
				
				repeat_rows_list = last_inner_append(repeat_rows_list, row,0,cur_depth);
				cur_depth = cur_depth - 1;
				repeat_rows_list = last_inner_append(repeat_rows_list,'',0,cur_depth);
			elif row['field_name'].find(' repeat ') != -1:
				repeat_info = row['field_name'].strip().split();
				row['field_name'] = repeat_info[0];
				form_list.append(''.join(repeat_info[3:]));

				repeat_rows_list = last_inner_append(repeat_rows_list, [row],0,cur_depth);
				cur_depth = cur_depth - 1;
				repeat_rows_list = last_inner_append(repeat_rows_list,'',0,cur_depth);
			elif len(repeat_rows_list) > 0:
				repeat_rows_list = last_inner_append(repeat_rows_list, row,0,cur_depth);
			
			if cur_depth <= 0 and len(repeat_rows_list) > 0:
				"""
				Run if there are values in the repeat_rows_list but the current depth
				is 0, meaning all startrepeats have been closed with endrepeats
				"""
				repeat_rows_list = clean_list_space(repeat_rows_list);
				repeat_rows_list = clean_list_endrepeat(repeat_rows_list);
				create_form_relations(repeat_rows_list,form_list,0,0);
				repeat_rows_list = order_list(repeat_rows_list);
				all_repeats.append(repeat_rows_list);
				repeat_rows_list = [];	
				form_list = [''];
				cur_depth = 0;
			elif cur_depth <= 0 and len(repeat_rows_list) == 0:
				#Print a row normally
				fout.write(generateJson(row));
				fout.write('\n');
				cur_depth = 0;
				form_list = [''];
				repeat_rows_list = [];
		#print last repeats list, if any
		if row['form_name'] != last_form_name:
			if last_form_name:
				print_list(all_repeats, fout);
				all_repeats = [];
		return fout.name;

	def clean_list_space(self, repeats_list):
		"""
		Removes all values in a list that equal ''.
		If there are nested lists, it recursively calls itself to search those
		too.
		"""
		for j,item in enumerate(repeats_list):
			if isinstance(item,list):
				item = clean_list_space(item);
			elif item == '':
				repeats_list.pop(j);
		return repeats_list;

	def clean_list_endrepeat(self, repeats_list):
		"""
		Removes all values in a list where the field_name = 'endrepeat'.
		If there are nested lists, the function is recursively called to
		search them too.
		"""
		for j, item in enumerate(repeats_list):
			if isinstance(item,list):
				item = clean_list_endrepeat(item);
			elif item['field_name'] == 'endrepeat':
				repeats_list.pop(j);
		return repeats_list;

	def create_form_relations(self, repeats_list, form_list, form_index, prev_form_index):
		"""
		Edit form names to include the previous form read, so models can reference
		each other through foreign keys. If there are nested lists, the function is 
		recursively called to search them too.
		"""
		num_lists = 0;
		for j, item in enumerate(repeats_list):
			if isinstance(item,list):
				num_lists = num_lists + 1;
				item = create_form_relations(item, form_list, form_index+num_lists, form_index);
			else:
				item['form_name'] = form_list[form_index] + '~' + form_list[prev_form_index];

	def order_list(self, repeats_list):
		"""
		Given a repeats list created in the csv2json function, this list will pull out all
		the embedded lists and order them in order of appearence, while keeping values in their
		correct list, even if they were seperated by another list.
		"""
		orderList = [[]];
		for j,item in enumerate(repeats_list):
			if isinstance(item,list):
				orderList.append(order_list(item));
			else:
				orderList[0].append(item);
		return orderList;		

	def print_list(self, someList, fout):
		"""
		Prints every value in someList, including values in nested lists
		"""
		for item in someList:
			if isinstance(item,list):
				print_list(item,fout);
			else:	
				fout.write(generateJson(item));
				fout.write('\n');

	def last_inner_append(self,x,y,curDepth,depth):
		"""
		Finds the deepest index in a list, that is not a list itself. If a list is 
		found, the function is called recursively on that list.
		"""
		try:
			if(curDepth != depth):
				if isinstance(x[-1],list):
					last_inner_append(x[-1],y,curDepth+1,depth);
					return x;
		except IndexError:
			pass;
		x.append(y);
		return x;

	def generateJson(self, row):
		"""
		Generates the json for the given row. The json is formatted to 1 line for easier
		search when generating the django models.
		"""
		return (json.dumps({'form':
	                                        {'form name': row['form_name'],
	                                        'section header': row['section_name'],
	                                        'field':
       		                                 {'field name': row['field_name'],
       	        	                          'field label': row['field_label'],
                	                         'field note': row['field_note'],
                	                         'type':
                	                                {'field type': row['field_type'],
                        	                         'choices': row['choices']},
                        	                 'text validation':
                        	                        {'validation type': row['validation_type'],
	                                                 'min value': row['min_value'],
        	                                         'max value': row['max_value']},
                	                         'identifier': row['is_identifier'],
                        	                 'branching logic': row['branching_logic'],
                                	         'required?': row['required'],
                                        	 'alignment': row['custom_alignment'],
                                         	'question number': row['question_number'],
       		                                 },},},indent=0, separators=(',',':')));	
	
	def json2dj(self, fileName):
		form2model = lambda form_name: form_name.title().replace('_','').replace(' ','').replace('-','');
	
		fout = open(fileName + '.py', 'w+');

		prev_form_name = None;
	prev_fk_name = None;
	for line in open(fileName,'r'):
		form_name = get_field_value(line, 'form name');
		fk_name = None;
		
		#print form_name;
		if form_name.find('~') != -1:
			form_name, fk_name = form_name.split('~');
			fk_name = form2model(fk_name);
			form_name = form2model(form_name);
			#print 'fk_name ' + str(fk_name) + '	' + 'prev_fk ' + str(prev_fk_name);
			if form_name != prev_form_name:
				if prev_fk_name:
					fout.write(get_FK(prev_fk_name));
				if prev_form_name:
					for meta_line in get_meta(prev_form_name):
						fout.write(meta_line);
				prev_form_name = form_name;
				prev_fk_name = fk_name;
				fout.write('class %s(models.Model):' % form_name);
				fout.write('\n');
				
			column_name = get_field_value(line, 'field name');
			att_name = column_name.lower();
			comment_notes = [];
			extra_params = {};
	
			extra_params['verbose_name'] = get_field_value(line, 'field label');
			
			extra_params['help_text'] = get_field_value(line, 'field note');
			
			if ' ' in att_name or '-' in att_name or keyword.iskeyword(att_name) or column_name != att_name:
				extra_params['db_column'] = column_name;
			
			if ' ' in att_name:
				att_name = att_name.replace(' ','_');
				comment_notes.append('Field renamed to remove spaces.');
			if '-' in att_name:
				att_name = att_name.replace('-','_');
				comment_notes.append('Field renamed to remove dashes.');
			if column_name != att_name:
				comment_notes.append('Field name made lowercase.');
		
			field_type, field_params, field_notes = get_field_type(line);
			extra_params.update(field_params);
			comment_notes.extend(field_notes);
		
			field_type += '('

			if keyword.iskeyword(att_name):
				att_name += '_field';
				comment_notes.append('Field renamed because it was a Python reserved word.');
			if att_name[0].isdigit():
				att_name = 'number_%s' % att_name;
				extra_params['db_column'] = unicode(column_name);
				comment_notes.append("Field renamed because it wasn't a valid python identifier.");
		
			if att_name == 'id' and field_type == 'AutoField(' and extra_params == {'primary_key': True}:
			continue
			field_desc = '%s = models.%s' % (att_name, field_type);
			if extra_params:
				if not field_desc.endswith('('):
					field_desc += ', ';
				field_desc += ', '.join(['%s=%r' % (k, v) for k, v in extra_params.items()])
			field_desc += ')';
			if comment_notes:
				field_desc += ' # ' + ' '.join(comment_notes);
		
			fout.write('    %s\n' % field_desc);
		#final meta class
		if fk_name:
			fout.write(get_FK(fk_name));
		for meta_line in get_meta(form_name):
			fout.write(meta_line);

	def get_field_type(self, line):
		"""
		Given the database connection, the table name, and the cursor row description,
		this routine will return the given field type name, as well as any additional keyword
		parameters and notes for the field.
		"""
		field_params = {};
		field_notes = [];
	
		required = get_field_value(line,'required?');
		validation_type = get_field_value(line,'validation type');
		field_type = get_field_value(line,'field type');

		try:
			field_type = field_types.get(validation_type, field_types[field_type]);
		except KeyError:
			field_type = 'TextField';
			field_notes.append('This field type is a guess');
		if not required:
			field_params['blank'] = True
			if field_type is 'BooleanField':
				field_type = 'NullBooleanField';
			else:
				field_params['null'] = True;
		if field_type == 'CharField':
			field_params['max_length'] = 2000;

		choices = None;
		if get_field_value(line,'choices'):
			try:
				choices = [(int(v.strip()), k.strip()) for v, k in [choice.split(',') \
					for choice in get_field_value(line,'choices').split('|')]]
				field_type = 'IntegerField'
			except (ValueError, TypeError):
				pass
		
		if choices:
			field_params['choices'] = choices;
	
		return field_type, field_params, field_notes;

	def get_field_value(self, line, field):
		"""
		Determines the value of a field from the json representation.
			
		This function first finds the begining of the field name (not the value).
		Then adds the length of the field to the index, and then adds another 3 to it. 
		The additional 3 come from the way the Json is structured. A typical Json 'field' 
		looks like this example: "identifier":"some_value". The added 3 index comes from 
		the second quotation mark, the colon, and the third quotation.
		
		Then finds the length of the field_value and returns that substring using the determined indices.
		"""
		field_index = line.find('"' + field + '"');
		field_index = field_index + len(field) + 4;
		current_char = line[field_index];
		field_len = 0;
		while current_char != '"':
			field_len += 1;
			current_char = line[field_index+field_len];
		field_value = line[field_index:field_index+field_len];
		return field_value;
	
	def get_FK(self, form_name):
		return '    ' + form_name.lower() + ' = models.ForeignKey(' + form_name + ')\n';

	def get_meta(self, table_name):
		"""	
		Return a sequence comprising the lines of code necessary
		to construct the inner Meta class for the model 
		corresponding to the given database table name.
		"""
		return ['\n',
			'    class Meta:\n',
			'	 db_table = %r\n' % table_name,
			'\n',
			'\n'];

if len(sys.argv) > 1:
	readFile(sys.argv[1]);
else:
	readFile();
