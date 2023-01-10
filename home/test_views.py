from django.test import TestCase


class TestHomeViews(TestCase):

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_get_delivery_page(self):
        response = self.client.get('/delivery')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/delivery.html')

    def test_get_privacy_page(self):
        response = self.client.get('/privacy')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/privacy.html')
