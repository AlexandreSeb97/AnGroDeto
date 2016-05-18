from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.http import Http404
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext
from datetime import datetime
from models import Atik, AutoLink

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
        {'atiks': atik},
        context_instance=RequestContext(request,
            {
                'title': 'Atik ki dispo sou AnGroDeto',
                'year': datetime.now().year,
                'date': datetime.now().date(),
            })
    )


def autolink_blog(request):
    # Pran tout machin yo
    auto = AutoLink.objects.filter(published=True)
    "Renders the Autolink page"
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'autolink.html',
        {'autos': auto},
        context_instance=RequestContext(request,
        {
            'title': 'Machin ki pou vann nan AutoLink',
            'year': datetime.now().year,
            'date': datetime.now().date(),
            'a': 1,
        })
    )


def atik(request, slug):
    atik = get_object_or_404(Atik, slug=slug)
    # return the rendered atik
    return render(request, 'atik.html', {'atik': atik})


def auto(request, slug):
    auto = get_object_or_404(AutoLink, slug=slug)
    # return the rendered auto
    return render(request, 'auto.html', {'auto': auto})
