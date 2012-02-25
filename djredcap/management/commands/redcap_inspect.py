import csv
import keyword
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
    'is_indentifier',
    'branching_logic',
    'required',
    'custom_alignment',
    'question number',
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
    """
    SYNOPSIS::

        python manage.py redcap inspect [options...] file

    DESCRIPTION:

        Attempts to parse a REDCap data dictionary and output Django models
        that match the data dictionary's rules.

    OPTIONS:

        ``--version`` - pass the REDCap version number of the CSV file

    """

    help = """Attempts to parse a REDCap data dictionary and output Django
    models that match the data dictionary's rules.
    """

    requires_model_validation = False

    db_module = 'django.db'

    args = 'filename'

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.form_names = []

    def handle(self, filename=None, *args, **options):
        if not filename:
            raise CommandError('Enter a filename')

        fin = open(filename)
        dialect = csv.Sniffer().sniff(fin.read(1024))
        fin.seek(0)
        reader = csv.DictReader(fin, fieldnames=header_keys, dialect=dialect)
        # Skip header
        reader.next()

        for line in self.handle_inspection(reader):
            self.stdout.write("%s\n" % line)

    def handle_inspection(self, reader):
        yield "# This is an auto-generated Django model module."
        yield "# You'll have to do the following manually to clean this up:"
        yield "#     * Make sure each model has one field with primary_key=True"
        yield "#     * Ensure each model has a OneToOneField with the main model"
        yield "# Feel free to rename the models, but don't rename db_table values or field names."
        yield ''
        yield 'from %s import models' % self.db_module
        yield ''

        table2model = lambda table_name: table_name.title().replace('_', '').replace(' ', '').replace('-', '')

        for i, row in enumerate(reader):
            table_name = row['form_name']

            if table_name not in self.form_names:
                self.form_names.append(table_name)
                if i != 0:
                    for meta_line in self.get_meta(table_name):
                        yield meta_line
                yield 'class %s(models.Model):' % table2model(table_name)

            column_name = row['field_name']
            att_name = column_name.lower()
            comment_notes = [] # Holds Field notes, to be displayed in a Python comment.
            extra_params = {}  # Holds Field parameters such as 'db_column'.

            extra_params['verbose_name'] = row['field_label']

            if row['field_note']:
                extra_params['help_text'] = row['field_note']


            # If the column name can't be used verbatim as a Python
            # attribute, set the "db_column" for this Field.
            if ' ' in att_name or '-' in att_name or keyword.iskeyword(att_name) or column_name != att_name:
                extra_params['db_column'] = column_name

            # Modify the field name to make it Python-compatible.
            if ' ' in att_name:
                att_name = att_name.replace(' ', '_')
                comment_notes.append('Field renamed to remove spaces.')

            if '-' in att_name:
                att_name = att_name.replace('-', '_')
                comment_notes.append('Field renamed to remove dashes.')

            if column_name != att_name:
                comment_notes.append('Field name made lowercase.')

            # Calling `get_field_type` to get the field type string and any
            # additional paramters and notes.
            field_type, field_params, field_notes = self.get_field_type(row)
            extra_params.update(field_params)
            comment_notes.extend(field_notes)

            field_type += '('

            if keyword.iskeyword(att_name):
                att_name += '_field'
                comment_notes.append('Field renamed because it was a Python reserved word.')

            if att_name[0].isdigit():
                att_name = 'number_%s' % att_name
                extra_params['db_column'] = unicode(column_name)
                comment_notes.append("Field renamed because it wasn't a "
                    "valid Python identifier.")

            # Don't output 'id = meta.AutoField(primary_key=True)', because
            # that's assumed if it doesn't exist.
            if att_name == 'id' and field_type == 'AutoField(' and extra_params == {'primary_key': True}:
                continue

            field_desc = '%s = models.%s' % (att_name, field_type)
            if extra_params:
                if not field_desc.endswith('('):
                    field_desc += ', '
                field_desc += ', '.join(['%s=%r' % (k, v) for k, v in extra_params.items()])
            field_desc += ')'
            if comment_notes:
                field_desc += ' # ' + ' '.join(comment_notes)
            yield '    %s' % field_desc

        # Output the final Meta class
        if self.form_names:
            for meta_line in self.get_meta(table_name):
                yield meta_line

    def get_field_type(self, row):
        """Given the database connection, the table name, and the cursor row
        description, this routine will return the given field type name, as
        well as any additional keyword parameters and notes for the field.
        """
        field_params = {}
        field_notes = []

        required = row['required']
        validation_type = row['validation_type']
        field_type = row['field_type']

        try:
            field_type = field_types.get(validation_type, field_types[field_type])
        except KeyError:
            field_type = 'TextField'
            field_notes.append('This field type is a guess.')

        if not required:
            field_params['blank'] = True
            if field_type is 'BooleanField':
                field_type = 'NullBooleanField'
            else:
                field_params['null'] = True

        if field_type == 'CharField':
            field_params['max_length'] = 2000

        choices = None
        if row['choices']:
            try:
                choices = [(int(v.strip()), k.strip()) for v, k in [choice.split(',') \
                    for choice in row['choices'].split('|')]]
                field_type = 'IntegerField'
            except (ValueError, TypeError):
                pass

        if choices:
            field_params['choices'] = choices

        return field_type, field_params, field_notes

    def get_meta(self, table_name):
        """Return a sequence comprising the lines of code necessary
        to construct the inner Meta class for the model corresponding
        to the given database table name.
        """
        return ['',
                '    class Meta:',
                '        db_table = %r' % table_name,
                '',
                '']
