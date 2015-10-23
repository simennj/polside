from django.conf.urls import url
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    url(r'^$', views.liste),
    url(r'^liste/$', RedirectView.as_view(url='/pol/', permanent=False)),
    # url(r'^(?P<x>[0-9]+)/$', views.topX, name='topX'),
    url(r'^table$', views.table),
    url(r'^produkt/(?P<pk>[0-9]+)/$', views.Produktvisning.as_view(), name='Produkt'),
    url(r'^produktside/(?P<pk>[0-9]+)/$', views.Produktside.as_view(), name='Produkt'),
]
