from django.conf.urls import url, include
from reviews.views import new_review 

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', new_review, name='new-review'),
]
