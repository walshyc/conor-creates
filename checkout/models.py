from django.db import models
from services.models import Service

class Order(models.Model):
    name = models.CharField(max_length=50, blank = False)
    contact_number = models.CharField(max_length = 25, blank = False)
    address1 = models.CharField(max_length = 50, blank = False)
    address2 = models.CharField(max_length = 50, blank = True)
    town = models.CharField(max_length = 50, blank = False)
    county = models.CharField(max_length = 40, blank = False)
    postcode = models.CharField(max_length = 15, blank = True) 
    country = models.CharField(max_length = 50, blank = False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null = False)
    service = models.ForeignKey(Service, null = False)
    quantity = models.IntegerField(blank = False)

    def __str__(seld):
        return "{0} {1} @ {2}".format(self.quantity, self.service.name, self.service.price)
    