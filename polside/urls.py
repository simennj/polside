"""polsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.http import HttpResponse
from django.views.generic.base import RedirectView

from pol import views


urlpatterns = [
    url(r'^google089c2d1580aaed24.html$',
        lambda request: HttpResponse('google-site-verification: google089c2d1580aaed24.html')),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^pol/', RedirectView.as_view(url='/', permanent=False)),
    url(r'^', include('pol.urls')),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/$', views.TestViewSet.as_view()),
    url(r'^bolrest/$', views.BolRestView.as_view()),
]
