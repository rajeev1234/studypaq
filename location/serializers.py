from rest_framework import serializers

from .models import Locations


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = ['id', 'location_id', 'location_name']