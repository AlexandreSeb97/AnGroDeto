from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.http import Http404
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext
from datetime import datetime
from models import Atik

# Create your views here.

#HomePage view
def index(request):
    "Renders the home page"
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'cover.html',
        context_instance=RequestContext(request,
        {
            'title': 'Home',
            'year': datetime.now().year,
            'date': datetime.now().date,
        })
    )


# Atik Blog view
def atik_blog(request):
    # Pran tout atik yo
    atik = Atik.objects.filter(published=True)
    "Renders the Atik page"
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'atik_blog.html',
        {'atiks':atik},
        context_instance=RequestContext(request,
            {
                'title': 'Atik ki dispo sou AnGroDeto',
                'year': datetime.now().year,
                'date': datetime.now().date(),
            })
    )


def atik(request, slug):
    atik = get_object_or_404(Atik, slug=slug)
    # return the rendered atik
    return render(request, 'atik.html', {'atik': atik})
