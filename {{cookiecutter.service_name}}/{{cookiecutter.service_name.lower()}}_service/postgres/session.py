from axial.postgres.util import scoped_session_factory

from {{cookiecutter.service_name.lower()}}_service.config import settings


# Thread-local database session
Postgres = scoped_session_factory(
        settings['postgres']['url'],
        pool_size=settings['postgres']['pool_size'],
        )
