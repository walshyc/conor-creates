from django.db import models
from django.contrib.auth.models import User
from services.models import Service


class Review(models.Model):
    user = models.ForeignKey(User, default="1", null=False, on_delete=models.DO_NOTHING)
    service = models.ForeignKey(Service, null=False)
    date = models.DateField()
    comments = models.TextField(default="", blank=False)
    approved = models.BooleanField(default=False)
    

    def __str__(self):
        return "{0}-{1}-{2}-{3}-{4}".format(self.user, self.date, self.service, self.comments, self.approved)