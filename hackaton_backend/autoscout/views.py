from django.shortcuts import render
from models import trip_entry
from serializers import TripEntrySerializer
from rest_framework import generics


class EntryList(generics.ListCreateAPIView):
    queryset = trip_entry.objects.all()
    serializer_class = TripEntrySerializer
