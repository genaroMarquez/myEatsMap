from .models import Entry
from rest_framework import serializers

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['id','added_by', 'added_date', 'venue_type', 'venue_name', 'street_address', 'city',
                  'state', 'zipcode', 'lng', 'lat', 'geo_address', 'score',]