from django.contrib import admin

from places.models import LocationPhoto
from places.models import Coordinates, Location, LocationPhoto


class LocationPhotoTabularInline(admin.TabularInline):
    model = LocationPhoto
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        return obj.image_tag


class CoordinatesTabularInline(admin.TabularInline):
    model = Coordinates


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    inlines = [LocationPhotoTabularInline, CoordinatesTabularInline]


# admin.site.register(LocationPhoto)
# admin.site.register(Coordinates)
