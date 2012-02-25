django-redcap
=============

Utilities for porting REDCap projects to and from Django models.

Install and Setup
-----------------
django-redcap is available on [PyPi][0]. Use Pip to install it:

```bash
pip install django-redcap
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
Commands are executed using the `redcap` command with a sub-command, e.g.:

```bash
./manage.py redcap [options] subcommand [args]
```

**inspect**

```bash
./manage.py redcap inspect path/to/exported/data_dictionary.csv > models.py
```
