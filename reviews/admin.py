from django.contrib import admin
from reviews.models import Review
# adds the reviews to the admin part of the site
admin.site.register(Review)