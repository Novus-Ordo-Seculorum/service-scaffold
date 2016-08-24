import pytz

from datetime import datetime

from axial.service.endpoint import Endpoint, HandlerConfig

from .schemas import ApiStatusSchema


class StatusCheck(Endpoint):

    path = '/status'

    get_v1 = HandlerConfig(
        response=ApiStatusSchema,
        )

    def on_get_v1(self, request, response):
        return {
            'name': '{{cookiecutter.service_name.lower()}}',
            'datetime': str(datetime.now(pytz.utc)),
            }
