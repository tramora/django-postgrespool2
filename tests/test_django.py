from django.test import TestCase
from django.utils import timezone
from .models import DogModel


class TestPool(TestCase):
    databases = {"default", "psycopg"}

    def test_simple_request(self):
        DogModel.objects.create(name='wow')
        DogModel.objects.create(name='gog')

    def test_datetime(self):
        _ = DogModel.objects.create(name="wow", created=timezone.now())
        dog1 = DogModel.objects.using("default").get(name="wow")
        dog2 = DogModel.objects.using("psycopg").get(name="wow")
        self.assertEqual(dog1.created, dog2.created)
