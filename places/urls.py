from django.urls import include, path

from places.views import LocationListView


urlpatterns = [
    path("", LocationListView.as_view({"get": 'location'}), name="location"),
]
