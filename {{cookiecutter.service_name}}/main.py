"""
uWSGI mountpoint:
The uwsgi.ini points to this module, expecting to find the callable, `app`.
"""

from {{cookiecutter.service_name}}_service import Application


app = Application('{{cookiecutter.service_name}}')
"""The uWSGI mountpoint."""
