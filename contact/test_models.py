from django.test import TestCase
from .models import ContactForm


class TestContactModels(TestCase):

    def test_string_representation(self):
        contact = ContactForm(contact_email="test@email.com")
        self.assertEqual(str(contact), contact.contact_email)

    def test_replied_defaults_to_false(self):
        contact_form = ContactForm.objects.create(
            contact_name="test name",
            contact_email="test@test.com",
            contact_phone_number="123345",
            contact_message="this is a test message",
        )
        self.assertFalse(contact_form.replied)
