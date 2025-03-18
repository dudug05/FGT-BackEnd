from django.db import models

from .customer import Customer
from .product import Product
from .service import Service

class Budget(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.PROTECT, related_name="Budget_customers", null=True, blank=True
    )
    date_budget = models.DateField()
    product = models.ManyToManyField(Product, blank=True)
    service =  models.ForeignKey(
        Service, on_delete=models.PROTECT, related_name="Budget_service", null=True, blank=True
    )
    price_budget = models.DecimalField(max_digits=10, decimal_places=2)

    def total(self):

        return sum([product.price_budget for product in self.product.all()])

    def __str__(self):
        products = ", ".join([str(product) for product in self.product.all()])
        return f'Budget {self.id}: {self.customer} - {self.date_budget} - {self.service} - {self.product} '
