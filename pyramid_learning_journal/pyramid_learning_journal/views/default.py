"""Define functions to handle my routes."""

from pyramid.view import view_config
from ..models.mymodel import MyModel


@view_config(route_name="home", renderer="pyramid_learning_journal:templates/index.jinja2")
def list_view(request):
    """Handle a request for the  list view."""
    entries = request.dbsession.query(MyModel).order_by(MyModel.date.desc()).all()
    return {
        "entries": entries
    }


@view_config(route_name="details", renderer="pyramid_learning_journal:templates/details.jinja2")
def detail_view(request):
    """Handle a request for the detail view."""
    entry_id = int(request.matchdict['id'])
    entry = request.dbsession.query(MyModel).get(entry_id)
    return {
        "entry": entry
    }


@view_config(route_name="create", renderer="pyramid_learning_journal:templates/new.jinja2")
def create_view(request):
    """Handle a request for the create view."""
    return {}


@view_config(route_name="update", renderer="pyramid_learning_journal:templates/edit.jinja2")
def update_view(request):
    """Handle a request for the update view."""
    entry_id = int(request.matchdict['id'])
    entry = request.dbsession.query(MyModel).get(entry_id)
    return {
        "entry": entry
    }
