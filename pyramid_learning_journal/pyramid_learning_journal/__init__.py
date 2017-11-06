"""Define the main function, which kicks off this whole ball of wax."""


from pyramid.config import Configurator


def main(global_config, **settings):
    """Start the app."""
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('.views')
    config.include('.routes')
    config.scan()
    return config.make_wsgi_app()
