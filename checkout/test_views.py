from django.test import TestCase


class TestCheckoutViews(TestCase):

    def test_get_checkout_page_empty_bag(self):
        bag = {}

        response = self.client.get('/checkout/', )
        self.assertEqual(response.status_code, 302)
