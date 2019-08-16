from django.db import models
from django.contrib.auth.models import User
from services.models import Service

class SingleOrder(models.Model):
    user = models.ForeignKey(User, default="1", null=False, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50, blank = False)
    contact_number = models.CharField(max_length = 25, blank = False)
    email = models.EmailField(max_length=100, blank = False, default = "")
    date = models.DateField()
    brief = models.TextField(default="", blank = False)
    # upload = models.FileField(upload_to="uploads", default="")

    def __str__(self):
        return "{0}-{1}-{2}-{3}-{4}".format(self.id, self.date, self.name, self.brief, self.user)

class SingleOrderUpload(models.Model):
    order = models.ForeignKey(SingleOrder, related_name='upload')
    uploaded_file = models.FileField(upload_to = 'images')


class SingleOrderLineItem(models.Model):
    order = models.ForeignKey(SingleOrder, null = False)
    service = models.ForeignKey(Service, null = False)
    quantity = models.IntegerField(blank = False)


    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.service.name, self.service.price)
    