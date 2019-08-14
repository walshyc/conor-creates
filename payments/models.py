from django.db import models
from services.models import Service

class SingleOrder(models.Model):
    name = models.CharField(max_length=50, blank = False)
    contact_number = models.CharField(max_length = 25, blank = False)
    address1 = models.CharField(max_length = 50, blank = False)
    address2 = models.CharField(max_length = 50, blank = True)
    town = models.CharField(max_length = 50, blank = False)
    county = models.CharField(max_length = 40, blank = False)
    postcode = models.CharField(max_length = 15, blank = True) 
    country = models.CharField(max_length = 50, blank = False)
    date = models.DateField()
    brief = models.TextField(default="", blank = False)
    # upload = models.FileField(upload_to="uploads", default="")

    def __str__(self):
        return "{0}-{1}-{2}-{3}".format(self.id, self.date, self.name, self.brief)

class SingleOrderUpload(models.Model):
    order = models.ForeignKey(SingleOrder, related_name='upload')
    uploaded_file = models.FileField(upload_to = 'images')


class SingleOrderLineItem(models.Model):
    order = models.ForeignKey(SingleOrder, null = False)
    service = models.ForeignKey(Service, null = False)
    quantity = models.IntegerField(blank = False)


    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.service.name, self.service.price)
    