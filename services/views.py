from django.shortcuts import render, get_object_or_404
from .models import Service, ServiceImage

def all_services(request):
    services = Service.objects.all()
    images = ServiceImage.objects.all()
 
    return render(request, 'services.html', {'services': services, 'images': images})

def single_service(request, pk):
    service = get_object_or_404(Service, pk=pk)    

    return render(request, 'single-service.html', {'service': service})