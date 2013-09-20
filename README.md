django-redcap
=============

Utilities for porting REDCap projects to and from Django models.

What it does
------------

[Djredcap] (https://github.com/dmegahan/django-redcap) and [djfixture] (https://github.com/cbmi/djFixture) are 2 scripts that automate the process of transferring patient or survey data from Redcap to Harvest. The programs work alongside one another to create a models.py file, a fixtures.json file and a filename.json file. 

When djredcap is run on a data dictionary from redcap, it will iterate through each line in the file, grouping each field (a line in a data dictionary describes a field) by their form names and printing each form as a json object. The json file outputted by djredcap now contains each form, with every field grouped into a form. Djredcap then iterates through the forms in the json file and builds the model.py file by reading each fields information and constructing the models.py file form by form.

Install and Setup
-----------------

**Dependencies**

`inflect`

```bash
easy_install inflect
```
--------------------
To install:

1. Download django-redcap from github
2. Enter /django-redcap/ and do

```bash
python setup.py sdist
cd dist
tar xvfz django-redcap-0.1.12b2.tar.gz
cd django-redcap-0.1.12b2
python setup.py install --user
```

Once installed, simply add `djredcap` to your `INSTALLED_APPS` project settings:

```python
INSTALLED_APPS = (
    'djredcap',
    ...
)
```

Commands
--------

Djredcap and djfixture function alongside one another. For both of them to work correctly, they must be run in the correct order. djredcap should be run first. Djredcap creates an intermediary json file that describes each form, including each field and its information, from the redcap data dictionary submitted in djredcap. This json file is used in djfixture to describe the models.py file.

Commands are executed using the `redcap` command with a sub-command, e.g.:

```bash
./manage.py redcap [options] subcommand [args]
```

**inspect**

The basic command. The inspect command takes in a redcap data dictionary and outputs a
models.py file based on the dictionary, along with an intermediate JSON file describing 
the data dictionary.
```bash
./manage.py redcap inspect path/to/exported/data_dictionary.csv
```
**convert**

The convert command takes the data dictionary and directly writes to models.py. 
The json file that would normally be output (inspect) is not created.

```bash
./manage.py redcap convert path/to/exported/data_dictionary.csv
```
**models**

The models command takes the intermediate JSON file and writes a models.py file based on it.

```bash
./manage.py redcap models path/to/generated/json_file.json
```
**json**

The json command takes the data dictionary from redcap as input and outputs an intermediate JSON file.
```bash
./manage.py redcap json path/to/exported/data_dictionary.csv
```
**fixture**

The fixture command creates a django data fixture from a redcap data file, a JSON intermediate file(generated
from inspect or json commands) and a django project name. The name of the outputted file is fixtures.json.
```bash
./manage.py redcap fixture path/to/exported/data_file.csv path/to/generated/json_file.json django_project_name
```

How to use it
-------------
You will need a REDCap data dictionary (.csv). A data dictionary would be a file that 
describes the fields in the database you are looking to create a model of. Each line in a data dictionary would 
be a description of a field, from its name, form, branching logic, type, etc.

Use the inspect command to create a models.py file from the REDCap data dictionary. 
For example:
```bash
./manage.py redcap inspect data_dictionary.csv
```
Outputted will be a json file named after the data dictionary and the models.py file. The json intermediate is
currently used to create a fixtures.json file, since it is schema based on the model.

To create a fixtures.json file to go along with your models.py file, you will need a REDCap data file (.csv) that
contains data from the matching database, the matching intermediate file created from running the inspect or json
commands, and the name of your django project.

```bash
./manage.py redcap fixture data.csv intermediate.json projectname
```

How it works
-------------

djredcap
========

There are 2 main parts to djredcap. The function(csv_2_json) that generates the json file from the 
data dictionary, and the function(json_2_dj) that generates the models.py file from the intermediate json
file.

**csv_2_json**

[csv_2_json](https://github.com/cbmi/django-redcap/blob/master/djredcap/management/subcommands/djredcap.py#L51), in the simplest terms, parses through the data dictionary, line by line, and groups the fields in the dictionary by their form name, while retaining the rest of the field information.

*Non-repeating fields*
Non-repeating fields are simple. When a new form is found by reading the fields information, a json syntactic form, 
which the form's information and empty list of fields, is generated([generate_json_form](https://github.com/cbmi/django-redcap/blob/master/djredcap/management/subcommands/djredcap.py#L405)). Each field in that form is added to that list([generate_json_field](https://github.com/cbmi/django-redcap/blob/master/djredcap/management/subcommands/djredcap.py#L415)). Once a different form is started, [the previous form is printed](https://github.com/cbmi/django-redcap/blob/master/djredcap/management/subcommands/djredcap.py#L93).

*Repeating fields*
This is done by constructing lists of lists of lists of fields, called repeating_rows, based on their form names 
and if they are a part of repeating groups. A repeating group is a group of fields, where the first field in the group has startrepeat "num" "new form name" and the last field in the group has endrepeat. A repeating group can be 
nested inside another repeating group, and so on. repeating_rows mirrors the nesting, by creating the same relationship inside lists of lists([last_inner_append](https://github.com/cbmi/django-redcap/blob/master/djredcap/management/subcommands/djredcap.py#L301)). 

Once all the endrepeats have been matched up with startrepeats(there is no more repeating fields), repeating_rows is cleaned of any junk fields(clean_list,blank fields created by last_inner_append or fields that only contain "endrepeat") and each form is related to the form it is nested inside by create_form_relations. Each list in repeating_rows is then ordered by appearance in the list([order_list](https://github.com/cbmi/django-redcap/blob/master/djredcap/management/subcommands/djredcap.py#L232)).

Repeating_rows is then appended to all_repeats, which holds all the repeating rows in the current form. Once a new field form is encountered, all_repeats is printed([95](https://github.com/cbmi/django-redcap/blob/master/djredcap/management/subcommands/djredcap.py#L94)).


**json_2_dj**

[json_2_dj](https://github.com/cbmi/django-redcap/blob/master/djredcap/management/subcommands/djredcap.py#L440) works by loading in each json form, read from the intermediary created before, and reading each field in it. 
The first thing printed is the form information(class form_name). If the form name contains a ‘~’, then it was a 
repeating form and a foreign key field is created. A string, to be printed, is created based on the fields 
“attributes”, like field type, field note, field label, field name, etc. The field is then printed to the models.py.


djfixture
=========

[djfixture](https://github.com/cbmi/django-redcap/blob/master/djredcap/management/subcommands/djfixture.py) uses the json intermediary to retrieve the relevant data from the REDCap data csv. 
Each form in the json file is parsed, one by one. Once a form has been read in, the program reads through each line 
in the data csv, which corresponds to an individual record. If a form is a repeating form, the number of repeats is 
stored and the name of the forms it relates to is stored in list([93](https://github.com/cbmi/django-redcap/blob/master/djredcap/management/subcommands/djfixture.py#L93)).  

The [generate_repeating_fixtures](https://github.com/cbmi/django-redcap/blob/master/djredcap/management/subcommands/djfixture.py#L158) function is then called. This function creates a number of fixtures, based on the 
number of repeats, and populates them with data. This is done by looping through each field in the form, determining 
the matching field in the data file by using the field’s name and type ([get_field_name](https://github.com/cbmi/django-redcap/blob/master/djredcap/management/subcommands/djfixture.py#L344), [get_field_names](https://github.com/cbmi/django-redcap/blob/master/djredcap/management/subcommands/djfixture.py#L391)). Once the 
right field has been found, the data and field name are stored in a fixture and added to a list of fixtures ([289](https://github.com/cbmi/django-redcap/blob/master/djredcap/management/subcommands/djfixture.py#L289), [335](https://github.com/cbmi/django-redcap/blob/master/djredcap/management/subcommands/djfixture.py#L335)).
Once all forms have been parsed and the fixture list has been populated, it is printed ([print_fixtures](https://github.com/cbmi/django-redcap/blob/master/djredcap/management/subcommands/djfixture.py#L455)). 



More in-depth comments can be found in djredcap and djfixture.


