# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from django.views import generic
from rest_framework import filters
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from pol.forms import *
from pol.models import *
from pol.serializers import ProduktSerializer


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
    if side is None:
        side = ""
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


class TestViewSet(generics.ListAPIView):
    queryset = Produkter.objects.filter(produktutvalg__contains="Ba")
    serializer = ProduktSerializer
    serializer_class = serializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ProduktFilter
    #pagination_class = LargeResultsSetPagination
#    def get(self, request, format=None):
#        f = ProduktFilter(request.GET, queryset=Produkter.objects.filter(produktutvalg__contains="Ba"))
#        paginator = Paginator(f, 5)
#        side = request.GET.get('side')
#        try:
#            produkter = paginator.page(side)
#        except PageNotAnInteger:
#            produkter = paginator.page(1)
#        except EmptyPage:
#            produkter = paginator.page(paginator.num_pages)
#        serializer = ProduktSerializer(produkter, many=True)
#        return Response(serializer.data)


class Produktside(generic.DetailView):
    model = Produkter
    template_name = 'produktside.html'


class Produktvisning(generic.DetailView):
    model = Produkter
    template_name = 'produktvisning.html'
