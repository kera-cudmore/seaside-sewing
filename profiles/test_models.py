from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile


class TestProfilesModels(TestCase):

    def test_string_representation(self):
        user = User(username="username test")
        self.assertEqual(str(user), user.username)
