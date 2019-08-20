from django.test import TestCase
from about.forms import ContactUsForm

class TestContactForm(TestCase):

    def test_send_email_with_a_name(TestCase):
        form = ContactUsForm(
            {'name': 'Test Name'}
        )

        self.assertTrue(form.is_valid())
