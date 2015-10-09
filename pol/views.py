# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.views import generic

from pol.forms import *
from pol.models import *


def index(request):
    return render(request, 'index.html')


def topX(request, x):
    toppliste = Produkter.objects.filter(produktutvalg='Basisutvalget').order_by('enhetspris')[:int(x)]
    return render(request, 'topX.html', {
        'toppliste': toppliste,
    })

def liste(request):
    varenavnform = VarenavnForm(request.GET)
    varetypeform = VaretypeForm(request.GET)
    prisform = PrisForm(request.GET)
    volumform = VolumForm(request.GET)
    alkoholform = AlkoholForm(request.GET)
    enhetsprisform = EnhetsprisForm(request.GET)
    sorteringsform = SorteringsForm(request.GET)
    f = ProduktFilter(request.GET, queryset=Produkter.objects.all())[:100]
    return render_to_response('liste.html', {
        'filter': f,
        'varenavnform': varenavnform,
        'varetypeform': varetypeform,
        'prisform': prisform,
        'volumform': volumform,
        'alkoholform': alkoholform,
        'enhetsprisform': enhetsprisform,
        'sorteringsform': sorteringsform,
    })

def table(request):
    varenavnform = VarenavnForm(request.GET)
    varetypeform = VaretypeForm(request.GET)
    prisform = PrisForm(request.GET)
    volumform = VolumForm(request.GET)
    alkoholform = AlkoholForm(request.GET)
    enhetsprisform = EnhetsprisForm(request.GET)
    sorteringsform = SorteringsForm(request.GET)
    f = ProduktFilter(request.GET, queryset=Produkter.objects.all())[:100]
    return render_to_response('table.html', {
        'filter': f,
        'varenavnform': varenavnform,
        'varetypeform': varetypeform,
        'prisform': prisform,
        'volumform': volumform,
        'alkoholform': alkoholform,
        'enhetsprisform': enhetsprisform,
        'sorteringsform': sorteringsform,
    })


class Produktside(generic.DetailView):
    model = Produkter
    template_name = 'produktside.html'


class Produktvisning(generic.DetailView):
    model = Produkter
    template_name = 'produktvisning.html'


def map(request):
    return render(request, 'map.html')
