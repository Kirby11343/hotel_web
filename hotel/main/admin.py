from django.contrib import admin


from .models import *

class AuthUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'is_active', 'is_superuser', 'is_staff', 'role', 'date_joined', 'last_login')
    list_display_links = ('id',)
    search_fields = ('id', 'username', 'email')
    list_editable = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_superuser', 'is_staff', 'role',)

class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_user', 'phone_number')
    list_display_links = ('id',)
    search_fields = ('id', 'phone_number')
    list_editable = ('id_user', 'phone_number')
    list_filter = ('id_user',)



admin.site.register(Phone, PhoneAdmin)
admin.site.register(AuthUser, AuthUserAdmin)