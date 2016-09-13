import pytz

from datetime import datetime

from axial.service.route import Route, handler_config

from .schemas import StatusSchema


class Status(Route):
    path = '/status'

    @handler_config(
        response=StatusSchema,
        )
    def on_get_v1(self, request, response):
        return {
            'name': '{{cookiecutter.service_name.lower()}}',
            'status': 'ok'
            }
