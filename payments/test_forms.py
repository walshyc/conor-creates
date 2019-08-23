from django.test import TestCase
from payments.forms import SingleOrderForm, SinglePayForm


class TestOrderForm(TestCase):

    def test_order_valid_with_all_fields(self):
        form = SingleOrderForm(
            {'name': 'test name',
             'contact_number': '0874524',
             'email': 'test@test.com',
             'primary_color': '#000000',
             'secondary_color': '#ffffff',
             'brief': 'test brief'}
        )
        self.assertTrue(form.is_valid())

    def test_order_no_name(self):
        form = SingleOrderForm(
            {
                'contact_number': '0874524',
                'email': 'test@test.com',
                'primary_color': '#000000',
                'secondary_color': '#ffffff',
                'brief': 'test brief'}
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], ['This field is required.'])

    def test_order_no_contact_number(self):
        form = SingleOrderForm(
            {'name': 'test name',
             'email': 'test@test.com',
             'primary_color': '#000000',
             'secondary_color': '#ffffff',
             'brief': 'test brief'}
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['contact_number'], [
                         'This field is required.'])

    def test_order_no_email(self):
        form = SingleOrderForm(
            {'name': 'test name',
             'contact_number': '0874524',
             'primary_color': '#000000',
             'secondary_color': '#ffffff',
             'brief': 'test brief'}
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['This field is required.'])

    def test_order_no_primary_color(self):
        form = SingleOrderForm(
            {'name': 'test name',
             'contact_number': '0874524',
             'email': 'test@test.com',
             'secondary_color': '#ffffff',
             'brief': 'test brief'}
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['primary_color'], [
                         'This field is required.'])

    def test_order_no_secondary_color(self):
        form = SingleOrderForm(
            {'name': 'test name',
             'contact_number': '0874524',
             'email': 'test@test.com',
             'primary_color': '#000000',
             'brief': 'test brief'}
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['secondary_color'], [
                         'This field is required.'])

    def test_order_no_brief(self):
        form = SingleOrderForm(
            {'name': 'test name',
             'contact_number': '0874524',
             'email': 'test@test.com',
             'primary_color': '#000000',
             'secondary_color': '#ffffff'
             }
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['brief'], ['This field is required.'])


class TestPaytForm(TestCase):
    def test_make_payment_form(self):
        form = SinglePayForm(
            {'credit_card_number': '',
             'cvv': '',
             'expiry_month': ''})
        self.assertFalse(form.is_valid())
