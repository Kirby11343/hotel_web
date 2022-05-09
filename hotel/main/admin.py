from django.contrib import admin

from .models import *

class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_user', 'phone_number')
    list_display_links = ('id',)
    search_fields = ('id', 'phone_number')
    list_editable = ('id_user', 'phone_number')
    list_filter = ('id_user',)


admin.site.register(Phone, PhoneAdmin)
