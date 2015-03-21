from django.shortcuts import render
from models import trip_entry
from serializers import TripEntrySerializer
from rest_framework import generics


# Create your views here.
class EntryMixin(object):
    
    queryset = trip_entry.objects.all()
    serializer_class = TripEntrySerializer



class EntryList(EntryMixin, generics.ListCreateAPIView):
    pass
