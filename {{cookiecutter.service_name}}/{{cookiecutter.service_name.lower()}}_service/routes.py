import pytz

from datetime import datetime

from axial.service.route import Route, HandlerConfig

from .schemas import ApiStatusSchema


class StatusCheck(Route):

    path = '/status'

    get_v1 = HandlerConfig(
        response=ApiStatusSchema,
        )

    def on_get_v1(self, request, response):
        return {
            'name': '{{cookiecutter.service_name.lower()}}',
            'datetime': str(datetime.now(pytz.utc)),
            }
