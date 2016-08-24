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
    from . import endpoints

    if middleware_enabled:
        middleware = [
            EncoderDecoder(processors=[
                ProtobufProcessor(__package__),
                JsonProcessor(),
                ]),
            SqlalchemyConnector(Postgres),
            ]
    else:
        middleware = None

    endpoints=[
        endpoints.ApiStatus(),
        ]

    return App(
        settings['service'],
        middleware=middleware,
        endpoints=endpoints)
