from django.test import TestCase
from .models import Product, sum

# Create your tests here.


class ProductTest(TestCase):
    def setUp(self):
        Product.objects.create(name="Mobile", price=323.99, description="Just Mobile")

    def test_product_name(self):
        self.first = Product.objects.get(name="Mobile")
        ide = self.first.id
        self.assertEqual(ide, 1)

    # def test_description(self):
    #     desc = self.first.description
    #     self.assertEquals(desc, 'False')
    #
    # def test_price_(self):
    #     price = self.first.price
    #     self.assertEquals(price, 33)
class SumTest(TestCase):
    def test_sum(self):
        self.assertEquals(sum(4,8), 12)
        self.assertEquals(sum(5,5), 10)
        self.assertEquals(sum(3,6), 9)
        self.assertEquals(sum(8,6), 7)
