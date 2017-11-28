"""Define the main function, which kicks off this whole ball of wax."""

import os
from pyramid.config import Configurator


def main(global_config, **settings):
    """Start the app."""
    if os.environ.get('DATABASE_URL', ''):
        settings['sqlalchemy.url'] = os.environ['DATABASE_URL']
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('.views')
    config.include('.routes')
    config.include('.models')
    config.scan()
    return config.make_wsgi_app()
