from django.conf.urls import url, include

from . import views


from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'produkter', views.ProduktVisningsSet, 'Produkter')

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<x>[0-9]+)/$', views.topX, name='topX'),
    url(r'^liste$', views.liste),
    url(r'^table$', views.table),
    url(r'^test$', views.tabletest),
    url(r'^produkt/(?P<pk>[0-9]+)/$', views.ProduktVisning.as_view(), name='Produkt'),
    url(r'^', include(router.urls)),
    url(r'^map', views.map)
]
