from django.conf.urls import patterns, url, include

from .views import NoteListView

urlpatterns = patterns('',
    url(r'^$', NoteListView.as_view(), name='list'),
)
