from typing import Dict

from django.urls import reverse
from django.conf import settings
from django.db.models import QuerySet

from  places.models import Location


def get_geo_json(locations: QuerySet[Location]) -> Dict:
    GEO_JSON = {
        "type": "FeatureCollection",
        "features": []
    }
    for location in locations:
        data = {
            "type": "Feature",
            "geometry": {"type": "Point"},
            "properties": {}
        }
        endpoint = reverse('places',kwargs = {'pk':location.id})
        data['geometry']['coordinates'] = [float(location.coordinates.langitude), float(location.coordinates.lotitude)]
        data['properties']['title'] = location.title
        data['properties']['placeId'] = location.id
        data['properties']['detailsUrl'] = settings.LOCAL_ADDRESS + endpoint
        GEO_JSON["features"].append(data)
    return GEO_JSON
