from django.conf.urls import patterns, url
from django.views.generic import TemplateView, ListView

from artist_catalog import views


urlpatterns = patterns('',
    url(r'^artists/$', views.ArtistList.as_view(), name='ArtistsList'),
    url(r'^artist/(?P<pk>\d+)$', views.ArtistDetail.as_view(), name='ArtistDetail'),
    url(r'^artwork/$', views.ArtworkList.as_view(), name='ArtworkList'),
)

