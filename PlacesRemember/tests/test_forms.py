from django.test import TestCase
from PlacesRemember.forms import PlaceForm
from PlacesRemember.models import Place
from django.contrib.auth.models import User


class TestForms(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='TestUserName',
            password='TestPassword',
            is_active=True,
            is_staff=True,
            is_superuser=True
        )

    def test_place_form_valid_data(self):
        form = PlaceForm(data={
            'name': 'TestName',
            'geom': '{"type":"Point", "coordinates":[56.013976,92.852635]}',
            'comment': 'TestComment'
        })

        self.assertTrue(form.is_valid())

    def test_place_form_save_data(self):

        form = PlaceForm(data={
            'name': 'TestName',
            'geom': '{"type":"Point", "coordinates":[56.013976,92.852635]}',
            'comment': 'Testcomment'
        })
        form.is_valid()
        new_place = form.save(self.user)

        self.assertEquals(Place.objects.first().name, 'Test Name')
        self.assertEquals(
            Place.objects.first().location.json,
            '{ "type": "Point", "coordinates":[56.013976,92.852635]}'
        )
        self.assertEquals(Place.objects.first().comment, 'TestComment')
