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
This will be a step by step explanation on how djredcap and djfixture work.
