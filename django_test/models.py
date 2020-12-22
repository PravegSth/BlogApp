from django.db import models
from django.urls import reverse

# Create your models here.



class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return f"{self.name} -> {self.price}"

    def get_absolute_url(self):
        return reverse('product-list')


def sum(a,b):
    return a+b

