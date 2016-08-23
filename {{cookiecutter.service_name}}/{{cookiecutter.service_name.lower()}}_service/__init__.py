def wsgi_app(ignore_middleware=False):
    from axial.service.app import App
    from axial.service.middleware import processors
    from axial.service import middleware

    from .config import settings
    from .db.session import Postgres
    from . import endpoints

    middleware = None
    if not ignore_middleware:
        middleware = [
            middleware.EncoderDecoder(processors=[
                processors.ProtobufProcessor(__package__),
                processors.JsonProcessor(),
                ]),
            middleware.SqlalchemyConnector(Postgres),
            ]

    endpoints=[
        endpoints.ApiStatus(),
        ]

    return App(
        __package__,
        middleware=middleware,
        endpoints=endpoints)
