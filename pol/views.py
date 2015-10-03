from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from pol.models import *


def index(request):
    return render(request, 'index.html')

def topX(request, x):
    toppliste = Produkter.objects.filter(produktutvalg='Basisutvalget').order_by('enhetspris')[:int(x)]
    return render(request, 'topX.html', {
        'toppliste': toppliste,
    })

def produkt(request,produktid):
    p = get_object_or_404(Produkter, pk=produktid)
    return render(request, 'produktside.html', {
        'produktid': produktid,
        'produktinfo': p,
    })
