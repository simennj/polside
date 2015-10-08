from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<x>[0-9]+)/$', views.topX, name='topX'),
    url(r'^liste$', views.liste),
    url(r'^table$', views.table),
    url(r'^produkt/(?P<pk>[0-9]+)/$', views.ProduktVisning.as_view(), name='Produkt'),
    url(r'^map', views.map)
]
