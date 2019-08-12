from django.db import models

class Service(models.Model):
    name = models.CharField(max_length = 100, default = '')
    description = models.TextField()
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    
    def __str__(self):
        return self.name
    

class ServiceImage(models.Model):
    service = models.ForeignKey(Service, related_name='images')
    image = models.ImageField(upload_to = 'images')
    