def wsgi_app(middleware_enabled=True):
    from axial.service.app import App
    from axial.service.middleware.processors import (
        ProtobufProcessor, JsonProcessor,
        )
    from axial.service.middleware import (
        EncoderDecoder, SqlalchemyConnector
        )

    from .config import settings
    from .db.session import Postgres
    from . import routes

    service_name = settings['service']

    if middleware_enabled:
        middleware = [
            EncoderDecoder(processors=[
                ProtobufProcessor(service_name),
                JsonProcessor(),
                ]),
            SqlalchemyConnector(Postgres),
            ]
    else:
        middleware = None

    routes=[
        routes.StatusCheck(),
        ]

    return App(
        service_name,
        middleware=middleware,
        routes=routes)
