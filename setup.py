import os
import sys

from setuptools import setup, find_packages

BASE_PACKAGE = 'djredcap'
version = __import__(BASE_PACKAGE).get_version()

install_requires = [
	'django>=1.4,<1.6',
]

kwargs = {
    'packages': find_packages(exclude=['tests', '*.tests', '*.tests.*', 'tests.*']),
    'include_package_data': True,

    'install_requires': install_requires,

    'test_suite': 'test_suite',

    'tests_require': [
	'coverage',
    ],

    'version': version,
    'name': 'django-redcap',
    'author': 'Byron Ruth',
    'author_email': 'ruthb@email.chop.edu', 
    'description': 'Utilities for porting REDCap data dictionaries to a JSON schema and a JSON schema to Django',
    'license': 'BSD',
    'keywords': 'redcap JSON django utils',
    'url': 'https://github.com/cbmi/django-redcap/',

    'classifiers': [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
}

setup(**kwargs)
