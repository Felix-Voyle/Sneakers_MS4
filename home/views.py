from django.shortcuts import render

from .contexts import home_context

# Create your views here.


def index(request):
    """A view to return the index page"""

    return render(request, 'home/index.html', home_context())
