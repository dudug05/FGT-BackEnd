from django.db import models


class Supplier(models.Model):
   name_supplier = models.CharField(max_length=100)
   description_supplier = models.CharField(max_length=100)
   sector_supplier = models.CharField(max_length=100)


   def __str__(self):
       return f"{self.name_supplier} - {self.description_supplier} - {self.sector_supplier}"  