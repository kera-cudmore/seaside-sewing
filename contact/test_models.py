from django.test import TestCase
from .models import ContactForm


class TestContactModels(TestCase):

    def test_string_representation(self):
        contact = ContactForm(contact_email="test@email.com")
        self.assertEqual(str(contact), contact.contact_email)
