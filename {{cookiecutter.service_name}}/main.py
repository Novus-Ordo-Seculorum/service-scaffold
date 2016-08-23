"""
uWSGI mountpoint:
The uwsgi.ini points to this module, expecting to find the callable, `app`.
"""

from {{cookiecutter.service_name}}_service import wsgi_app


app = wsgi_app()
"""The uWSGI mountpoint."""
