from django.contrib import admin
from .forms import *

from .models import *

class AuthUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'is_active', 'is_superuser', 'is_staff', 'user_role', 'date_joined', 'last_login')
    list_display_links = ('id',)
    search_fields = ('id', 'username', 'email')
    list_editable = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_superuser', 'is_staff', 'user_role',)

class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_user', 'phone_number')
    list_display_links = ('id',)
    search_fields = ('id', 'phone_number')
    list_editable = ('id_user', 'phone_number')
    list_filter = ('id_user',)

class AuthUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'is_active', 'is_superuser', 'is_staff', 'user_role', 'date_joined', 'last_login')
    list_display_links = ('id',)
    search_fields = ('id', 'username', 'email')
    list_editable = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_superuser', 'is_staff', 'user_role',)

class ReviewsAdmin(admin.ModelAdmin):
    form = ReviewsAdminForm
    list_display = ('id', 'author', 'content', 'timestamp_review')
    list_display_links = ('id',)
    search_fields = ('id', 'author', 'timestamp_review')
    list_editable = ('content',)


admin.site.register(Phone, PhoneAdmin)
admin.site.register(AuthUser, AuthUserAdmin)
admin.site.register(Reviews, ReviewsAdmin)