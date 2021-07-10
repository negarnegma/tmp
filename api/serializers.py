from rest_framework import serializers
from .models import MapPoint, Bluetooth


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapPoint
        fields = '__all__'


class MacLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bluetooth
        fields = '__all__'
