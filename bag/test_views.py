from django.test import TestCase
from products.models import Product


class TestBagViews(TestCase):

    def test_get_bag_page(self):
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_product_to_bag(self):
        product = Product.objects.create(
            sku='12334',
            name='Test Product',
            description='This is the description for a test product',
            price=12.99,
            stock=3,
            rating=3,
            colour='Blue',
        )

        response = self.client.post(
            f'/bag/add/{product.id}/',
            {'quantity': 1, 'redirect_url': 'view_bag'}
        )
        bag = self.client.session['bag']
        self.assertEqual(bag[str(product.id)], 1)

    def test_remove_product_from_bag(self):
        product = Product.objects.create(
            sku='12334',
            name='Test Product',
            description='This is the description for a test product',
            price=12.99,
            stock=3,
            rating=3,
            colour='Blue',
        )
        self.client.post(
            f'/bag/add/{product.id}/',
            {'quantity': 1, 'redirect_url': 'view_bag'}
        )
        response = self.client.post(f'/bag/remove/{product.id}/')
