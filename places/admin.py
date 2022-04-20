from django.contrib import admin

from places.models import LocationPhoto
from places.models import Coordinates, Location, LocationPhoto


class LocationPhotoTabularInline(admin.TabularInline):
    model = LocationPhoto

class CoordinatesTabularInline(admin.TabularInline):
    model = Coordinates


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    inlines = [LocationPhotoTabularInline, CoordinatesTabularInline]


# admin.site.register(LocationPhoto)
# admin.site.register(Coordinates)
