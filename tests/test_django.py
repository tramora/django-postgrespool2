from django.test import TestCase
from .models import DogModel


class TestPool(TestCase):

    def tearUP(self):
        DogModel.objects.create(name='wow')
        DogModel.objects.create(name='gog')

    def test_simple_request(self):
        pass

    def test_postgis(self):
        with self.settings(DATABASES={
            'default': {
                'ENGINE': 'django_postgrespool2.postgis',
                'NAME': 'postgrespool_test',
                'USER': 'postgres',
                'PASSWORD': '',
                'HOST': 'localhost',
            }
        }):
            DogModel.objects.all()
