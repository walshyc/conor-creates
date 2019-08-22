from django.db import models

# model that adds a service table to the database
class Service(models.Model):
    name = models.CharField(max_length = 100, default = '')
    description = models.TextField()
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    main_image = models.ImageField(upload_to = 'images')
    short = models.CharField(max_length = 50, default = '')
    
    
    def __str__(self):
        return self.name
    
# model to allow aditional images to the Service model
class ServiceImage(models.Model):
    service = models.ForeignKey(Service, related_name='images')
    add_image = models.ImageField(upload_to = 'images')
    