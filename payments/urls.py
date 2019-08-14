from django.conf.urls import url
from payments.views import payment

urlpatterns = [
    url(r"^$", payment , name="payment"),
    
]
