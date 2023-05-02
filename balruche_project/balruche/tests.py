from django.test import TestCase
from django.utils import timezone

from balruche.models import Site, MasterBox, Balance, BalRucheDat

class SiteTest(TestCase):
  
    def create_Site(self, name):
        return Site.objects.create(name=name)

    def test_Site_creation(self):
        w = self.create_Site("ENSAM, Esplanade des Arts & Métiers")
        self.assertTrue(isinstance(w, Site))
        print(w)
        #self.assertEqual(w.__unicode__(), w.title)
