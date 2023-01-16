from django.test import TestCase
from django.contrib.auth.models import User


class TestProfilesModels(TestCase):

    def test_string_representation(self):
        user = User(username="username test")
        self.assertEqual(str(user), user.username)
