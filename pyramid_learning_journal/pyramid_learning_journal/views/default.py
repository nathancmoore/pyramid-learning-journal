"""Define functions to handle my routes."""

from pyramid.response import Response
import os

HERE = os.path.abspath(__file__)
STATIC = os.path.join(os.path.dirname(os.path.dirname(HERE)))


def list_view(request):
    """Handle a request for the  list view."""
    with open(os.path.join(STATIC, 'templates/index.html')) as file:
        return Response(file.read())


def detail_view(request):
    """Handle a request for the detail view."""
    with open(os.path.join(STATIC, 'templates/detail.html')) as file:
        return Response(file.read())


def create_view(request):
    """Handle a request for the create view."""
    with open(os.path.join(STATIC, 'templates/new.html')) as file:
        return Response(file.read())


def update_view(request):
    """Handle a request for the update view."""
    with open(os.path.join(STATIC, 'templates/edit.html')) as file:
        return Response(file.read())
