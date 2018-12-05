"""moviebase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from movielist.views import MovieListView, MovieView
from showtimes.views import CinemaListView, CinemaView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^movies/$', MovieListView.as_view(), name='movie-list'),
    url(r'^movies/(?P<pk>[0-9]+)/$', MovieView.as_view(), name='movie-detail'),
    url(r'^cinemas/$', CinemaListView.as_view(), name='cinema-list'),
    url(r'^cinemas/(?P<pk>[0-9]+)/$', CinemaView.as_view(), name='cinema-detail')
]
