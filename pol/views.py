# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, get_list_or_404, render_to_response
from django.views import generic
from rest_framework import viewsets
from serializers import *
from pol.forms import *
from pol.models import *


def index(request):
    return render(request, 'index.html')


def topX(request, x):
    toppliste = Produkter.objects.filter(produktutvalg='Basisutvalget').order_by('enhetspris')[:int(x)]
    return render(request, 'topX.html', {
        'toppliste': toppliste,
    })


def tabletest(request):
    varenavnform = VarenavnForm(request.GET)
    varetypeform = VaretypeForm(request.GET)
    prisform = PrisForm(request.GET)
    volumform = VolumForm(request.GET)
    alkoholform = AlkoholForm(request.GET)
    enhetsprisform = EnhetsprisForm(request.GET)
    sorteringsform = SorteringsForm(request.GET)
    f = ProduktFilter(request.GET, queryset=Produkter.objects.all())[:100]
    return render_to_response('tabletest.html', {
        'filter': f,
        'request': request,
        'varenavnform': varenavnform,
        'varetypeform': varetypeform,
        'prisform': prisform,
        'volumform': volumform,
        'alkoholform': alkoholform,
        'enhetsprisform': enhetsprisform,
        'sorteringsform': sorteringsform,
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


class ProduktVisningsSet(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        f = ProduktFilter(self.request.GET, queryset=Produkter.objects.all())
        return f
    serializer_class = ProduktSerializer
