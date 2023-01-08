from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):

    def test_orderform_full_name_is_required(self):
        form = OrderForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(
            form.errors['full_name'][0], 'This field is required.')

    def test_orderform_email_is_required(self):
        form = OrderForm(
            {
                'full_name': 'A Name',
                'email': '',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(
            form.errors['email'][0], 'This field is required.')

    def test_orderform_phone_number_is_required(self):
        form = OrderForm(
            {
                'full_name': 'A Name',
                'email': 'email@email.com',
                'phone_number': '',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(
            form.errors['phone_number'][0], 'This field is required.')

    def test_orderform_street_address1_is_required(self):
        form = OrderForm(
            {
                'full_name': 'A Name',
                'email': 'email@email.com',
                'phone_number': '1234567890',
                'street_address1': '',
            })
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors.keys())
        self.assertEqual(
            form.errors['street_address1'][0], 'This field is required.')
