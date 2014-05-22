from django.views.generic import TemplateView

from rest_framework import generics

from .serializers import EntrySerializer
from .models import Entry

class Map(TemplateView):
    template_name = 'index.html'

class EntryList(generics.ListCreateAPIView):
    model = Entry
    serializer_class = EntrySerializer
