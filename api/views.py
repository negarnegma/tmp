from rest_framework import decorators, generics
from .serializers import MapSerializer, MacLocationSerializer
from .models import MapPoint, Bluetooth
from django.shortcuts import get_object_or_404
from utilities import responses, exceptions as authnz_exceptions


@decorators.authentication_classes([])
@decorators.permission_classes([])
class PointDetail(generics.ListAPIView):
    """
        Get point map detail
    """
    queryset = MapPoint.objects.all()
    serializer_class = MapSerializer

    # def get_queryset(self):
    #     name = self.kwargs.get('name')
    #     print(name)
    #     return MapPoint.objects.filter(name=self.kwargs.get('name'))
    #


@decorators.authentication_classes([])
@decorators.permission_classes([])
class MapLocations(generics.ListCreateAPIView):
    queryset = Bluetooth.objects.all()
    serializer_class = MacLocationSerializer
