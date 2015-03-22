from django.forms import widgets
from rest_framework import serializers
from models import trip_entry


class TripEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = trip_entry

