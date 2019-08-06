from django.conf.urls import url, include
from .views import all_services, single_service

urlpatterns = [
    url(r"^$", all_services, name="services"),
    url(r'^(?P<pk>\d+)/$', single_service, name='single-service'),
]
