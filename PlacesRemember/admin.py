from django.contrib import admin
from PlacesRemember.models import Place
from leaflet.admin import LeafletGeoAdmin


class PlaceAdmin(LeafletGeoAdmin):
    list_display = ['name', 'location']

admin.site.register(Place, PlaceAdmin) 