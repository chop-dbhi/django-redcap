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

```bash
./manage.py redcap inspect path/to/exported/data_dictionary.csv
```

