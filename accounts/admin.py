from django.contrib import admin
from accounts.models import Profile
# adds the Profile model to the admin page
admin.site.register(Profile)
