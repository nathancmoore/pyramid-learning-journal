"""Define functions to handle my routes."""

from pyramid.response import Response


def list_view(request):
    """Handle a request for the  list view."""
    with open("./templates/index.html") as file:
        return Response(file.read())


def detail_view(request):
    """Handle a request for the detail view."""
    with open("./templates/detail.html") as file:
        return Response(file.read())


def create_view(request):
    """Handle a request for the create view."""
    with open("./templates/new.html") as file:
        return Response(file.read())


def update_view(request):
    """Handle a request for the update view."""
    with open("./templates/edit.html") as file:
        return Response(file.read())
