from django.db import models

from .customer import Customer
from .service import Service
from .budget import Budget

class ServiceOrder(models.Model):
    date_serviceOrder = models.DateField(null=False)
    customer = models.ForeignKey(
        Customer, on_delete=models.PROTECT, related_name="ServiceOrder_customer", null=True, blank=True
    )
    budget = models.ForeignKey(
        Budget,on_delete=models.PROTECT, related_name="ServiceOrder_budget", null=True, blank=True
    )
    service = models.ForeignKey(Service, on_delete=models.PROTECT,related_name="ServiceOrder_service" ,null=True, blank=True)

def __str__(self):
    return f"{self.id} - {self.date_serviceOrder} - {self.customer} - {self.budget} - {self.service}"

