from django.contrib import admin
from payments.models import SingleOrder, SingleOrderLineItem, SingleOrderUpload

class SingleOrderLineAdminInline(admin.TabularInline):
    model = SingleOrderLineItem


class SingleOrderUploadInline(admin.TabularInline):
    model = SingleOrderUpload
    extra = 5


class SingleOrderAdmin(admin.ModelAdmin):
    inlines = (SingleOrderLineAdminInline, SingleOrderUploadInline, )



admin.site.register(SingleOrder, SingleOrderAdmin)



    

