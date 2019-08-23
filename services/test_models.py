from django.test import TestCase
from services.models import Service

class TestProductsModel(TestCase):

    def test_create_service(self):
        service = Service(name="Test Service",
                          description="Test description service",
                          price = 59)
        self.assertEqual(service.name, 'Test Service')
        self.assertEqual(service.description, "Test description service")
        self.assertEqual(service.price, 59)
        self.assertFalse(service.main_image)
        
