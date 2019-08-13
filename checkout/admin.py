from django.contrib import admin
from checkout.models import Order, OrderLineItem, OrderUpload

class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem


class OrderUploadInline(admin.TabularInline):
    model = OrderUpload
    extra = 5


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, OrderUploadInline, )



admin.site.register(Order, OrderAdmin)



    

