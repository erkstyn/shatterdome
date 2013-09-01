from django.shortcuts import render

def index(request):
    """ Render the main page of the site."""

    # TODO(chris): grab "InstagramPost" objects
    # here and put them in context.

    return render(
        request,
        'main/index.html'
    )
