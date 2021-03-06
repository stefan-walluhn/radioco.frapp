from django.db import IntegrityError
from django.test import TestCase
from radioco.frapp.models import Station


class StationModelTest(TestCase):

    def setUp(self):
        self.station = Station.objects.create(
            name="RadioCo Test Station",
            display_name="RadioCo",
            city="Halle (Saale)",
            description="Some radio station",
            website="http://radioco.example.com",
            logo_url="http://radioco.example.com/logo")

    def test_name(self):
        self.assertEqual("RadioCo Test Station", self.station.name)

    def test_display_name(self):
        self.assertEqual("RadioCo", self.station.display_name)

    def test_city(self):
        self.assertEqual("Halle (Saale)", self.station.city)

    def test_description(self):
        self.assertEqual("Some radio station", self.station.description)

    def test_website(self):
        self.assertEqual("http://radioco.example.com", self.station.website)

    def test_logo_url(self):
        self.assertEqual(
            "http://radioco.example.com/logo", self.station.logo_url)

    def test_singleton(self):
        with self.assertRaises(IntegrityError):
            Station.objects.create()
