# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from .models import Category

def menu_links(request):
    """Retrieve all categories for use in the menu."""
    links = Category.objects.all()
    return dict(links=links)
