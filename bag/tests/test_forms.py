from django.test import TestCase
from bag.forms import OrderForm


class TestBagForms(TestCase):
    def test_name_is_required(self):
        form = OrderForm({
            'order_number': 'test',
            'user_profile': 'test',
            'full_name': 'test',
            'email': 'test@test.com',
            'phone_number': '123456',
            'country': 'Australia',
            'postcode': '1234',
            'town_or_city': 'testvill',
            'street_address1': '12 test street',
            'street_address2': 'test ',
            'date': 'Aug. 27, 2020, 10:05 a.m.',
            'order_total': '123',
            'grand_total': '123',
            'original_bag': 'test',
            'stripe_pid': 'test',
            })
        self.assertTrue(form.is_valid())

    def test_fields_are_explict_in_form_meta(self):
        form = OrderForm()
        self.assertEqual(form.Meta.fields, ('full_name', 'email', 'phone_number', 'street_address1', 'street_address2', 'town_or_city', 'postcode', 'country'))

    def test_name_is_not_required(self):
        form = OrderForm({
            'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['full_name'], [u'This field is required.'])
