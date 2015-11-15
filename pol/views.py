# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from django.views import generic

from pol.forms import *
from pol.models import *


def liste(request):
    varenavnform = VarenavnForm(request.GET)
    varetypeform = VaretypeForm(request.GET)
    prisform = PrisForm(request.GET)
    volumform = VolumForm(request.GET)
    alkoholform = AlkoholForm(request.GET)
    enhetsprisform = EnhetsprisForm(request.GET)
    sorteringsform = SorteringsForm(request.GET)
    butikkategoriform = Butikkategoriform(request.GET)
    land = LandForm(request.GET)
    produsent = ProdusentForm(request.GET)
    side = request.GET.get('side')
    return render_to_response('liste.html', {
        'varenavnform': varenavnform,
        'varetypeform': varetypeform,
        'prisform': prisform,
        'volumform': volumform,
        'alkoholform': alkoholform,
        'enhetsprisform': enhetsprisform,
        'sorteringsform': sorteringsform,
        'butikkategoriform': butikkategoriform,
        'landform': land,
        'produsentform': produsent,
        'side': side
    })


def table(request):
    f = ProduktFilter(request.GET, queryset=Produkter.objects.filter(produktutvalg__contains="Ba"))
    paginator = Paginator(f, 25)

    side = request.GET.get('side')
    try:
        produkter = paginator.page(side)
    except PageNotAnInteger:
        produkter = paginator.page(1)
    except EmptyPage:
        produkter = paginator.page(paginator.num_pages)

    return render_to_response('table.html', {
        'produkter': produkter,
    })


class Produktside(generic.DetailView):
    model = Produkter
    template_name = 'produktside.html'


class Produktvisning(generic.DetailView):
    model = Produkter
    template_name = 'produktvisning.html'
