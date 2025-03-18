from django.db import models



class Product(models.Model):
    name_product = models.CharField(max_length=100)
    price_product = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_product = models.IntegerField(default=0)
    description_product = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.name_product} - {self.price_product} - {self.quantity_product} - {self.description_product}"
