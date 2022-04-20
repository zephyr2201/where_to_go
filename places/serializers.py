from typing import Dict, List
from django.conf import settings
from  rest_framework import serializers

from places.models import Location


class LocationDetailSerializer(serializers.ModelSerializer):
    imgs = serializers.SerializerMethodField()
    coordinates = serializers.SerializerMethodField()

    class Meta:
        model = Location
        fields = ['title', 'imgs', 'description_short', 'description_long', 'coordinates']
    
    def get_imgs(self, obj) -> List:
        imgs = []
        photos = obj.images.all()
        if photos:
            for photo in photos:
                imgs.append(settings.LOCAL_ADDRESS + photo.file.url)
        return imgs

    def get_coordinates(self, obj) -> Dict:
        coordinates = {
            "lng": obj.coordinates.langitude,
            "lat": obj.coordinates.lotitude
        }
        return coordinates
