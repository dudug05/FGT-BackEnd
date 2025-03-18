from django.db import models

from .customer import Customer
from .product import Product

class Service(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='Service_customer')
    issueDate_service = models.DateField(null=True, blank=True)
    deliveryDate_service = models.DateField(null=True, blank=True)
    typeService_service = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.customer} - {self.deliveryDate_service} - {self.issueDate_service} - {self.typeService_service} - {self.product}"
