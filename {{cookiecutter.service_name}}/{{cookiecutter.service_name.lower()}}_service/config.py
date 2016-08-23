settings = {
    'service': '{{cookiecutter.service_name.lower()}}',
    'postgres': {
        'url': 'postgresql+psycopg2://postgres@localhost/{{cookiecutter.service_name.lower()}}_service',
        'pool_size': 64,
    }
}
