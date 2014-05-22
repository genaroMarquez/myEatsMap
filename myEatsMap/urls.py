from django.conf.urls import patterns, url

from .views import Map, EntryList

urlpatterns = patterns('',
    url(r'^$', Map.as_view(), name='map'),
    url(r'^api/entries/$', EntryList.as_view(), name='entry-list'),
)

