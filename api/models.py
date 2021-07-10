from django.db import models
import uuid

from macaddress import default_dialect

# Create your models here.
dialect = default_dialect()
from macaddress.fields import MACAddressField


class MapPoint(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.CharField(max_length=100)

    def __str__(self):
        return "%s " % self.name


class Bluetooth(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    mac = MACAddressField(null=True, blank=True)
