from django.test import TestCase
from django.urls import reverse


class TestProfilesViews(TestCase):

    def test_404_error_if_no_profile(self):
        response = self.client.get('profile')
        self.assertEqual(response.status_code, 404)

    def test_logged_in_user_can_access_profile(self):
        login = self.client.login(
            username='testuser1',
            password='1X<ISRUkw+tuK'
        )
        response = self.client.get(reverse('profile'))
