from django.test import TestCase
from .models import Category, Product


class TestProductModels(TestCase):

    def test_string_representation(self):
        product = Product(name="Test Product Name")
        self.assertEqual(str(product), product.name)

    def test_category_verbose_name_plural(self):
        self.assertEqual(str(Category._meta.verbose_name_plural), "Categories")
