from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):

    def test_contactform_contact_name_is_required(self):
        form = ContactForm({'contact_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('contact_name', form.errors.keys())
        self.assertEqual(
            form.errors['contact_name'][0], 'This field is required.')
