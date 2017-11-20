"""Define functions to handle my routes."""

from pyramid.view import view_config
from ..models.mymodel import MyModel
from pyramid.httpexceptions import HTTPFound, HTTPBadRequest


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


@view_config(route_name="create", renderer="pyramid_learning_journal:templates/new.jinja2", permission="secret")
def create_view(request):
    """Handle a request for the create view."""
    if request.method == "POST":
        if not all([text in request.POST for text in ['title', 'body']]):
            raise HTTPBadRequest
        new_entry = MyModel(
            title=request.POST['title'],
            body=request.POST['body']
        )
        request.dbsession.add(new_entry)
        return HTTPFound(request.route_url('home'))

    return {}


@view_config(route_name="update", renderer="pyramid_learning_journal:templates/edit.jinja2", permission="secret")
def update_view(request):
    """Handle a request for the update view."""
    entry_id = int(request.matchdict['id'])
    entry = request.dbsession.query(MyModel).get(entry_id)

    if request.method == "GET":
        return{
            "title": "Update",
            "entry": entry
        }

    if request.method == "POST":
        entry.title = request.POST['title']
        entry.body = request.POST['body']
        request.dbsession.add(entry)
        request.dbsession.flush()
        return HTTPFound(request.route_url('details', id=entry.id))
