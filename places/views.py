from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from django.shortcuts import render


class LocationListView(GenericViewSet):
    serializer_class = None
    serializers = {}

    def get_serializer_class(self):
        serializers = {**self.serializers}
        if self.action in serializers:
            return serializers[self.action]

        return super().get_serializer_class()

    def location(self, request):
        return render(request, 'index.html')
