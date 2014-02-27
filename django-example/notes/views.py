#coding=utf-8

from django.views import generic

from .models import Note


class NoteListView(generic.ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'list.html'
