from django.test import TestCase, Client
from django.urls import reverse
from PlacesRemember.models import Place
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            username='TestUserName',
            password='TestPassword',
            is_active=True,
            is_staff=True,
            is_superuser=True
        )
        self.user.set_password('TestPassword')
        self.user.save()
        self.user = authenticate(
            username='TestUserName', password='TestPassword')
        login = self.client.login(
            username='TestUserName', password='TestPassword')

        self.places_url = reverse('places')
        self.create_place_url = reverse('create')

    def test_places_GET(self):

        response = self.client.get(self.places_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'PlacesRemember/places.html')

    def test_create_place_GET(self):

        response = self.client.get(self.create_place_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'PlacesRemember/place_create.html')

    def test_create_place_POST_adds_new_place(self):

        response = self.client.post(self.create_place_url, {
            'name': ['TestPlace'],
            'geom': ['{ "type": "Point", "coordinates": [ 56.013976, 92.852635 ] }',],
            'comment': ['TestComment']
        })

        self.assertEquals(response.status_code, 301)
        self.assertEquals(Place.objects.first().name, 'TestPlace')

    def test_create_place_POST_no_data(self):

        response = self.client.post(self.create_place_url)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(Place.objects.count(), 0)
