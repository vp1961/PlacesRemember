from django.test import SimpleTestCase
from django.urls import reverse, resolve
from PlacesRemember.views import places, PlaceCreate


class TestUrls(SimpleTestCase):

    def test_places_url_is_resolves(self):
        url = reverse('places')
        self.assertEquals(resolve(url).func, places)

    def test_create_place_url_is_resolves(self):
        url = reverse('create')
        self.assertEquals(resolve(url).func.view_class, PlaceCreate)
