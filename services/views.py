import random
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Service, ServiceImage

def all_services(request):
    services = Service.objects.all()
    service_images = services.all() 
 
    return render(request, 'services.html', {'services': services, 'images': service_images})

def single_service(request, pk):
    service = get_object_or_404(Service, pk=pk)
    service_images = service.images.all() 
    random_image = random.choice(service_images)

    return render(request, 'single-service.html', {'service': service, 'images': service_images, 'random': random_image})