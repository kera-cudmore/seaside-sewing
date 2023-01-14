from django.test import TestCase
from .models import Category, Product
from django.contrib.auth.models import User
from django.test.client import Client


class TestProductViews(TestCase):

    def test_get_products_page(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_add_product_page_user(self):
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 302)

    def test_get_add_product_page_admin(self):
        # Set up a superuser
        password = 'mypassword'
        superuser = User.objects.create_superuser(
            'superuser',
            'myemail@test.com',
            password
        )
        self.client.login(username=superuser.username, password=password)

        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed((response, 'products/add_product.html'))
