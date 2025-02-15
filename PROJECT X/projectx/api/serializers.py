from rest_framework import serializers
from .models import Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['device_id', 'latitude', 'longitude', 'timestamp']
