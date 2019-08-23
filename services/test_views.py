from django.test import TestCase
from services.models import Service


class TestViews(TestCase):

    def test_get_all_services(self):
        page = self.client.get("/services/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "services.html")
