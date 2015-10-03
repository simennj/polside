from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<x>[0-9]+)/$', views.topX, name='topX'),
    url(r'^produkt/(?P<produktid>[0-9]+)', views.produkt),
]
