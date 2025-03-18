from django.db import models


class Customer(models.Model):
   cpfcnpj_customer = models.CharField(max_length=18, blank=True, null=True)
   name_customer = models.CharField(max_length=100)
   fantasyName_customer = models.CharField(max_length=100, blank=True, null=True)
   email_customer = models.EmailField(blank=True, null=True)
   telephone_customer = models.CharField(max_length=15, blank=True, null=True)
   cep_customer = models.CharField(max_length=9, blank=True, null=True)
   address_customer = models.CharField(max_length=100, blank=True, null=True)
   homeNumber_customer = models.CharField(max_length=10, blank=True, null=True)
   neighborhood_customer = models.CharField(max_length=100, blank=True, null=True)
   city_customer = models.CharField(max_length=50, blank=True, null=True)
   state_customer = models.CharField(max_length=50, blank=True, null=True)


   def __str__(self):
       return f"{self.name_customer} - {self.cpfcnpj_customer} - {self.telephone_customer} - {self.email_customer} - {self.fantasyName_customer} - {self.cep_customer} - {self.address_customer} - {self.homeNumber_customer} - {self.neighborhood_customer} - {self.city_customer} - {self.state_customer}"
