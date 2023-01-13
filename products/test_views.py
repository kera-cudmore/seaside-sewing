from django.test import TestCase
from .models import Category, Product
from django.contrib.auth.models import User
from django.test.client import Client


class TestProductViews(TestCase):

    def test_get_products_page(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_add_product_page_admin(self):
        password = 'mypassword'
        superuser = User.objects.create_superuser(
            'superuser',
            'myemail@test.com',
            password
        )
        # You'll need to log in before you can send requests through the client
        self.client.login(username=superuser.username, password=password)
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed((response, 'products/add_product.html'))
