import csv
import json
import keyword
import sys

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
	'question_number',
	'repeat_tf',
	'repeat_num',
	'repeat_pointer'
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
def readFile(fileName=None):
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
def csv2json(reader, fileName):
	"""
		Function that converts csv file to valid json. 
	"""
	fout = open(fileName + '.json', "w+");
	
	last_form_name = None;
	for row in reader:
		form_name = row['form_name'];
		
		#if the row just has endrepeat in it, skip it
		if row['field_name'] is 'endrepeat':
			row = reader.nextLine();
		
		#if form_name != last_form_name:
		#	if last_form_name:
		#		fout.write('}\n');
		#	last_form_name = form_name
		#	fout.write('{\n');
		#	fout.write('\t"form name": ' + row['form_name'] + '\n');
		#	fout.write('\t"section header": ' + row['section_name'] + '\n');
		#
		"""
		Needed for special case csv's with repeats used, not needed otherwise.
		Determines if a field_name has startrepeat in it, then extracts the 
		number of repeats and the field it refers to.
		"""
		str_repeat_start = row['field_name'].find('startrepeat');
		if str_repeat_start != -1:
			row['repeat_tf'] = "True";
			row['repeat_num'] = row['field_name'][str_repeat_start+12];
			row['repeat_pointer'] = row['field_name'][str_repeat_start+14:];
			row['field_name'] = row['field_name'][:str_repeat_start-1];
		else:
			row['repeat_tf'] = "False";
			row['repeat_num'] = "";
			row['repeat_pointer'] = "";
		
		#generating the json
		fout.write(json.dumps({'form':
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
					 'repeats':
						{'repeat?': row['repeat_tf'],
						 'repeat num': row['repeat_num'],
						 'repeat pointer': row['repeat_pointer']},
					},},},indent=0, separators=(',',':')));
		fout.write('\n');
	return fout.name;

def json2dj(fileName):
	form2model = lambda form_name: form_name.title().replace('_','').replace(' ','').replace('-','');
	
	fout = open(fileName + '.py', 'w+');

	prev_form_name = None
	
	for line in open(fileName,'r'):
		form_name = get_field_value(line, 'form name');
		
		if form_name != prev_form_name:
			prev_form_name = form_name;
			fout.write('class %s(models.Model):' % form2model(form_name));
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
		fout.write('    %s' % field_desc);
		fout.write('\n');
def get_field_type(line):
	"""Given the database connection, the table name, and the cursor row description,
	this routine will return the given field type name, as well as any additional keyword
	parameters and notes for the field.
	"""
	field_params = {};
	field_notes = [];
	
	required = get_field_value(line,'required');
	validation_type = get_field_value(line,'validation_type');
	field_type = get_field_value(line,'field_type');
	
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
def get_field_value(line, field):
	"""
		Determines the value of a field from the json representation.
		
		This function first finds the begining of the field name (not the value).   		    Then adds the length of the field to the index, and then adds another 3 to i		t. The additional 3 come from the way the Json is structured. A typical Json 		    'field' looks like this example: "identifier":"some_value". The added 3 inde     		x come from the second quotation mark, the colon, and the third quotation.
		
		Then finds the length of the field_value and returns that substring using th		    e determined indices.
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
if len(sys.argv) > 1:
	readFile(sys.argv[1]);
else:
	readFile();
