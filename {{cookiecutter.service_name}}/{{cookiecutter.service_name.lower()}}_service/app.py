import axial.service

from axial.service.middleware.processors import (
    #ProtobufProcessor,  # TODO: Reenable protobuf when consul is implemented
    JsonProcessor,
    )
from axial.service.middleware import (
    EncoderDecoder, SqlalchemyConnector
    )

from .postgres import Postgres
from . import routes


class Application(axial.service.Application):

    @property
    def middleware(self):
        return [
            EncoderDecoder(processors=[
                #ProtobufProcessor(self.name),
                JsonProcessor(),
                ]),
            SqlalchemyConnector(Postgres),
            ]

    @property
    def routes(self):
        return [
            routes.StatusCheck(),
        ]
