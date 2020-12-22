from django.test import TestCase
from .views import ProductListView, ProductCreateView
from .models import Product

# Create your tests here.


class ProductListTest(TestCase):
    def setUp(self):
        self.item = ProductListView()

    def test_model_name(self):
        model = self.item.model
        self.assertEquals(model, Product)

    def test_template_name(self):
        template = self.item.template_name
        self.assertEquals(template, 'django_test/index.html')


class ProductCreateTest(TestCase):
    def setUp(self):
        self.item = ProductCreateView()

    def test_model_name(self):
        model = self.item.model
        self.assertEquals(model, Product)

    def test_template_name(self):
        template = self.item.template_name
        self.assertEquals(template, 'django_test/product_create.html')
