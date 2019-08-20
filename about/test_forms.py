from django.test import TestCase
from about.forms import ContactUsForm

class TestContactForm(TestCase):

    def test_send_email_with_only_a_name(self):
        form = ContactUsForm(
            {'name': 'Test Name'}
        )
        self.assertFalse(form.is_valid())

    def test_send_email_with_only_an_email(self):
        form = ContactUsForm(
            {'email': 'test@test.com'}
        )
        self.assertFalse(form.is_valid())
    
    def test_send_email_with_only_a_message(self):
        form = ContactUsForm(
            {'message': 'test message'}
        )
        self.assertFalse(form.is_valid())
    
    def test_send_email_with_only_a_message_and_name(self):
        form = ContactUsForm(
            {'name': 'Test Name',
            'message': 'test message'
            }
        )
        self.assertFalse(form.is_valid())

    def test_send_email_with_only_an_email_and_name(self):
        form = ContactUsForm(
            {'name': 'Test Name',
            'email': 'test@test.com'
            }
        )
        self.assertFalse(form.is_valid())
    
    def test_send_email_with_only_an_email_and_message(self):
        form = ContactUsForm(
            {'message': 'Test Message',
            'email': 'test@test.com'
            }
        )
        self.assertFalse(form.is_valid())

    def test_send_email_with_all_three(self):
        form = ContactUsForm(
            {'name':'test name',
            'message': 'Test Message',
            'email': 'test@test.com'
            }
        )
        self.assertTrue(form.is_valid())