from django.test import TestCase
from . models import Hood
class TestHood(TestCase):
    def setUp(self):
        
        self.hood = Hood(name = 'Clayworks',location='Kasarani',occupants_count= 150,admin= 'Prime', description = 'This is a test hood description',photo= 'clayworks.png', police_contact = 912, health_contact = 1234)
        self.hood.save()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.hood, Hood))
        
    def test_save_hood(self):
        hood = Hood.objects.all()
        self.assertTrue(len(hood)>0)
        
    def test_delete_hood(self):
        hoods = Hood.objects.all().delete()
        self.assertTrue(len(hoods)>0)
        
        
