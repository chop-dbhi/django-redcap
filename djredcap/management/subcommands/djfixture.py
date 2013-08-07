#!/usr/bin/python

import sys
import os
import csv
import json
import re
import math
from decimal import Decimal
from django.core.management.base import BaseCommand, CommandError

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

__project_name__ = ''

requires_model_validation = False
db_module = 'django.db'
args = 'file', 'jsonfile'


def csv_2_fixture(self, file, reader, json_models, p_name, fout):
    global __project_name__
    __project_name__ = p_name

    base_form_name = ''
    new_form_name = ''
    form_name = ''
    pk_num_list = []
    fixtures = []
    form_dict = {}
    file.seek(0)
    reader.next()
    pk_num = 0

    for form in open(json_models, 'r'):
        form = json.loads(form)
        form_name = form['form name']
        file.seek(0)
        reader.next()

        pk_num = 0
        num_repeats = ''
        primary_key_counter = 0
        if form_name.find('~') != -1:
            form_name, fk_name = form['form name'].split('~')
            form_dict[form_name] = fk_name
            num_repeats = form_name.split(' ')[1]
        else:
            base_form_name = form['form name']
            form_dict = {}
        for line in reader:
            pk_num += 1
            fixture_dict = {}
            if num_repeats:
                if num_repeats.isdigit() is False:
                    """
                    Handles special case where the number of repeats depends
                    on another field, usually labeled as formName
                    [relativeForm].
                    This field will not be in the form[fields] list.
                    form_name is changed to avoid errors regarding the number
                    of repeats as the code continues, specifically an error
                    might pop up in find_related_forms if it is not changed to
                    a number.
                    """
                    new_num_repeats = line[num_repeats.replace('[', '')
                                           .replace(']', '')]
                    if not new_num_repeats:
                        new_num_repeats = 0
                    #form_name is formatted like formName 5~otherForm 5 before
                    #this change
                    new_form_name = form_name.split('~')[0] \
                        .split(' ')[0] + ' ' + str(new_num_repeats)
                    form_dict[new_form_name] = fk_name
                if new_form_name:
                    foreign_forms_list = find_related_forms(self,
                                                            new_form_name,
                                                            form_dict)
                    new_form_name = ''
                else:
                    foreign_forms_list = find_related_forms(self,
                                                            form_name,
                                                            form_dict)
                full_form_list = foreign_forms_list[:]
                full_form_list.append(base_form_name)
                full_form_list = full_form_list[::-1]

                primary_key_counter = generate_repeating_fixtures(
                    self, line, form, full_form_list,
                    fixtures, pk_num, pk_num_list,
                    primary_key_counter
                    )
            else:
                #code for generating a fixture without foreign keys
                #not used currently with the addition of record form
                pk_num_list.append(pk_num)
                for field in form['fields']:
                    """
                    Determines if there are choices in the field,
                    what they are, and gets the
                    value for each of those fields that includes the choices
                    """
                    if field['choices']:
                        field_names = get_field_names(self, field, form_dict,
                                                      field['field name'])
                        checked_line = ''
                        answered = ''
                        for name in field_names:
                            try:
                                if len(field_names) > 1:
                                    if line[name] == '1':
                                        checked_line = name[-1]
                                        answered = True
                                    elif line[name] == '0':
                                        answered = True
                                else:
                                    if line[name]:
                                        checked_line = line[name]
                            except KeyError:
                                #print 'ERROR: NOT FOUND ' + name
                                                            #print field
                                                            #print field_names
                                pass

                        if checked_line:
                            fixture_dict[field['field name']] = [field,
                                                                 checked_line]
                        elif answered is True:
                            fixture_dict[field['field name']] = [field, '0']
                        else:
                            fixture_dict[field['field name']] = [field, '']
                    else:
                        try:
                            fixture_dict[field['field name']] = [
                                field,
                                line[field['field name']]
                                ]
                        except KeyError:
                            #print 'ERROR: NOT FOUND '+field['field name']
                            #print field
                            pass
                fixtures.append([form_name, fixture_dict])
    print_fixtures(self, fixtures, pk_num_list, fout)


def generate_repeating_fixtures(self, line, form,
                                form_list, fixtures, pk_num,
                                pk_num_list, primary_key_counter):
    """
    This function generates the fixture dictionaries for a repeating form.
    """
    num_repeats_all = 1
    num_repeats_list = []
    current_repeat_list = []
    counter = 0

    #populates current_repeat_list with 1s, amount equal to length of
    #form_list - 1
    current_repeat_list = [1] * len(form_list[1:])
    #determines number of repeats from items in form_list
    for item in form_list:
        if len(item.split(' ')) > 1:
            num_repeats_form = item.split(' ')[1]
            num_repeats_list.insert(0, num_repeats_form)
            num_repeats_all = int(num_repeats_all) * int(num_repeats_form)

    for i in range(num_repeats_all):
        primary_key_counter += 1
        fixture_dict = {}
        form_num_list = []
        fk_index = len(form_list)-2
        foreign_key = form_list[fk_index].lower().split(' ')[0].replace('_',
                                                                        '')
        if fk_index == 0:
            fixture_dict[foreign_key] = ['', pk_num]
        else:
            fk_num = int(math.ceil(primary_key_counter /
                                   float(num_repeats_list[0])))
            fixture_dict[foreign_key] = ['', fk_num]
        pk_num_list.append(primary_key_counter)
        for field in form['fields']:
            clean_field_name = re.sub('\${d\}', '', field['field name'])
            #form_list[0] and form_list[1] are both 'base forms'
            #form_list[0] is record, form_list[1] is the form name given for
            #each field without repeating
            if len(form_list[2:]) == 0:
                base_field_name = field['field name']
            else:
                base_field_name = get_field_name(self, field,
                                                 form_list[2:],
                                                 current_repeat_list).lower()
            if field['choices']:
                field_names = get_field_names(self, field,
                                              form_list[2:], base_field_name)
                checked_line = ''
                answered = ''
                for name in field_names:
                    try:
                        if len(field_names) > 1:
                            if line[name] == '1':
                                checked_line = name[-1]
                                answered = True
                            elif line[name] == '0':
                                answered = True
                        else:
                            if line[name]:
                                checked_line = line[name]
                    except KeyError:
                        #print 'ERROR: FIELD NOT FOUND ' + name
                        #print field
                        #print field_names
                        pass
                #if the line is checked, the number of the option is the answer
                if checked_line:
                    fixture_dict[clean_field_name] = [field, checked_line]
                elif answered is True:
                    fixture_dict[clean_field_name] = [field, '0']
                else:
                    fixture_dict[clean_field_name] = [field, '']
            else:
                try:
                    fixture_dict[clean_field_name] = [field,
                                                      line[base_field_name]]
                except KeyError:
                    #print 'ERROR: NOT FOUND ' + base_field_name
                    #print field
                    #print base_field_name
                    pass
        clean_form_name = form['form name'].split(' ')[0].replace('$', '')
        fixtures.append([clean_form_name, fixture_dict])

        cur_ind = len(current_repeat_list) - 1
        update_current_repeats(self, num_repeats_list[::-1],
                               current_repeat_list, cur_ind)

    return primary_key_counter


def get_field_name(self, field, form_list, repeat_num_list):
    """
    Loops through a list of forms. All forms are prefix forms except for the
    last form in form_list.
    """
    prefix = ''
    for i in range(len(form_list)):
        if i != len(form_list)-1:
            str_split = form_list[i].split(' ')
            name = str_split[0]
            name = re.sub('\d$', '', name)
            num_repeats = repeat_num_list[i]
            prefix = prefix + name + str(num_repeats) + '_'
        elif field['field name'].find('${d}') != -1:
            field_name = re.sub('\$\{d\}',
                                str(repeat_num_list[-1]),
                                field['field name'])
        else:
            field_name = field['field name'] + '' + str(repeat_num_list[-1])
    field_name = prefix + field_name
    return field_name


def find_related_forms(self, form_name, form_dict, foreign_forms=None):
    """
    Finds the form_name value in the form_dict. If it is found, the function
    will call itself using form_dict[form_name]. The form_dict is a dictionary
    with the keys being a form name and the value being the name of the form
    they have a foreign key relation with.
    Ex: form_dict['Microarray 1'] = 'Prior Gen Testing'
    This function will continue until no more related forms are found, and will
    return a list of them, in order from highest to deepest form relation
    """
    if foreign_forms is None:
        foreign_forms = []
    if form_name in form_dict and not form_name in foreign_forms:
        foreign_forms.append(form_name)
        find_related_forms(self, form_dict[form_name],
                           form_dict, foreign_forms)
    return foreign_forms


def get_field_names(self, field, form_dict, field_name=None):
    """
    Checkboxes and radio_other fields have multiple parts in the data csv,
    usually something like name1 name2 name3 for each checkbox/radio button
    that is pushable, but the info must be put into one field.

    This method finds the fields in the data file that are related to the field
    parameter. If it is a checkbox, it splits the possible choices and uses
    that to find the fields.
    If another special case for field names needs to be added, all that
    needs to be done is add an elif statement with the field type or variable
    it depends on.
    """
    choices_field_names = []
    if field['field type'] == 'checkbox' or \
       field['field type'] == 'checkbox_other' or \
       field['field type'] == 'checkbox_details':

        choices = field['choices'].split('|')
        for choice in choices:
            choices_field_names.append(field_name.lower() + '___' +
                                       choice.split(',')[0].strip(' '))
    else:
        choices_field_names.append(field_name.lower())
    return choices_field_names


def update_current_repeats(self, form_list, current_repeats_list, cur_index):
    """
    Updates the current_repeats_list depending on form_list([5,5,5] which
    is a list of numbers indicating the max number of repeats needed) and
    current_repeats_list([1,1,1] which is a list of numbers indicating what
    iteration the repeating is on). When function is first called, cur_index
    will be 0. Iterates the current_repeats_list like
    [1,1,1][1,1,2][1,1,3][1,2,1][1,2,2][1,2,3]

    if the element at cur_index in current_repeats_list is greater than or
    equal to the element in form_list at cur_index (Both of these are ints),
    then 'reset' the element in current_repeats_list.
    if the cur_index - 1 is not negative (still in bounds + cur_index is
    not first index) then recursively call update_current_repeats on
    cur_index - 1
    else add 1 to current_repeats_list[cur_index]
    """

    if int(current_repeats_list[cur_index]) >= int(form_list[cur_index]):
        current_repeats_list[cur_index] = 1
        if cur_index - 1 >= 0:
            cur_index -= 1
            update_current_repeats(self, form_list,
                                   current_repeats_list, cur_index)
    else:
        current_repeats_list[cur_index] += 1


def print_fixtures(self, fixtures_list, pk_list, fout):
    """
    fixtures_list is a list of lists. Each element is a list of
    [form name,fixture_dict]. Each element in fixture_dict
    is [field, field_val]

    function loops through each element in fixtures_list, then each
    key(element) in fixtures_list[i][1](a fixture_dict) and determines if its
    fields are blank. If they are not blank, the field is added to field_dict.

    field_dict is then printed all fields in each fixture_dict has been checked
    """
    all_json = []
    first_fix = True
    for i in range(len(fixtures_list)):
        field_dict = {}
        #if field has a value, print it
        for key in fixtures_list[i][1]:
            if fixtures_list[i][1][key]:
                field = fixtures_list[i][1][key][0]
                field_val = fixtures_list[i][1][key][1]
                if field:
                    field_dict[key] = cast_field(self, field, field_val)
                else:
                    #if it is just a foreign key
                    field_dict[key] = field_val
        all_json.append({'model': __project_name__ + '.' +
                        fixtures_list[i][0].replace('_', '') + '',
                        'pk': pk_list[i],
                        'fields': field_dict
                         })
    fout.write(json.dumps(all_json, indent=4, separators=(',', ': ')))


def get_field_type(self, field):
    """
    Given the database connection, the table name, and the cursor row
    description, this routine will return the given field type name,as well
    as any additional keyword parameters and notes for the field.
    """

    required = field['required']
    validation_type = field['validation type']
    field_type = field['field type']

    try:
        field_type = field_types.get(validation_type, field_types[field_type])
    except KeyError:
        field_type = 'TextField'
    if not required:
        if field_type is 'BooleanField':
            field_type = 'NullBooleanField'

        choices = None
        if field['choices']:
            try:
                choices = [(int(v.strip()),
                           k.strip()) for v, k in [choice.split(',')
                           for choice in field['choices'].split('|')]]
                field_type = 'IntegerField'
            except (ValueError, TypeError):
                pass
    return field_type


def cast_field(self, field, field_val):
    """
    Casts line[name] depending on the field_type
    """
    field_type = get_field_type(self, field)
    if field_type == 'CharField' or field_type == 'TextField':
        return str(field_val)
    elif field_type == 'IntegerField':
        if field_val and field_val.isdigit():
            return int(field_val)
    elif field_type == 'FloatField':
        try:
            return float(field_val)
        except:
            pass
    elif field_type == 'NullBooleanField':
        if field_val == '':
            return None
        elif field_val == '0':
            return False
        elif field_val == '1':
            return True
        else:
            return field_val
    elif field_type == 'BooleanField':
        if field_val:
            if field_val == '1':
                return True
            elif field_val == '0':
                return False
            else:
                return field_val
    elif field_type == 'DateField':
        if field_val:
            return field_val
    else:
        return field_val
