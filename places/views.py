from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.template.response import TemplateResponse

from places.models import Location
from places.services import get_geo_json
from places.serializers import LocationDetailSerializer


class LocationListView(GenericViewSet):
    serializer_class = LocationDetailSerializer
    serializers = {
        'places': LocationDetailSerializer,
        'location': LocationDetailSerializer
    }

    def get_serializer_class(self):
        serializers = {**self.serializers}
        if self.action in serializers:
            return serializers[self.action]

        return super().get_serializer_class()

    def get_queryset(self):
        queryset = Location.objects.all()
        return queryset

    def location(self, request):
        locations = self.get_queryset()
        geo_json = get_geo_json(locations)
        return TemplateResponse(request, 'index.html', context={'geo_json': geo_json})

    def places(self, request, pk: int):
        location = self.get_object()
        serializer = self.get_serializer_class()(location)
        return Response(serializer.data, status=status.HTTP_200_OK)
