from django.contrib import admin
from .models import Service, ServiceImage


class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 6


class ServiceAdmin(admin.ModelAdmin):
    inlines = [ ServiceImageInline, ]

# displays each service and its images on the admin page
admin.site.register(Service, ServiceAdmin)
