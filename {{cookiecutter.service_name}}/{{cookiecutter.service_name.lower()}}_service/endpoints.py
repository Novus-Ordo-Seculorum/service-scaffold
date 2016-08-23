import pytz

from datetime import datetime

from axial.service.endpoint import Endpoint, Meta

from .schemas import ApiStatusSchema


class ApiStatus(Endpoint):
    path = '/status'
    meta = {
        'GET': Meta(
            response_schema=ApiStatusSchema(),
            )
        }

    def on_get_v1(self, request, response):
        return {
            'name': '{{cookiecutter.service_name.lower()}}',
            'when': str(datetime.now(pytz.utc)),
            }
