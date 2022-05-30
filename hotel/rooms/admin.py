from django.contrib import admin
from .forms import *

class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm
    list_display = ('category_title', 'category_description', 'slug')
    list_display_links = ('category_title',)
    search_fields = ('category_title', 'slug')
    list_editable = ('category_description', 'slug')

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'room_type_title', 'room_number', 'category_title', 'maintenance_title', 'room_image', 'thumbnail_preview')
    list_display_links = ('id',)
    search_fields = ('id', 'room_type_title__room_type_title', 'room_number__room_number', 'category_title__category_title', 'maintenance_title__maintenance_title',)
    list_editable = ('room_type_title', 'room_number', 'category_title', 'maintenance_title', 'room_image')
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Мініатюра'
    thumbnail_preview.allow_tags = True

class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'price_id')
    list_display_links = ('room_number',)
    search_fields = ('room_number',)
    list_editable = ()

class PriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'numberofpeople', 'rate', 'room_type_fk')
    list_display_links = ('id',)
    search_fields = ('id', 'numberofpeople', 'room_type_fk__room_type_title')
    list_editable = ('numberofpeople', 'rate', 'room_type_fk')

class RoomTypeAdmin(admin.ModelAdmin):
    form = RoomTypeAdminForm
    list_display = ('room_type_title', 'content',)
    list_display_links = ('room_type_title',)
    search_fields = ('room_type_title',)
    list_editable = ('content',)

class MaintenanceAdmin(admin.ModelAdmin):
    form = MaintenanceAdminForm
    list_display = ('maintenance_title', 'maintenance_description', 'maintenance_price', 'category', 'pdf_file')
    list_display_links = ('maintenance_title',)
    search_fields = ('maintenance_title',)
    list_editable = ('maintenance_description', 'maintenance_price', 'category', 'pdf_file')

class MaintenanceOrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'maintenance', 'used_date', 'order', 'comment', 'is_paid_for', 'is_confirmed')
    list_display_links = ('id',)
    search_fields = ('id', 'maintenance__maintenance_title', 'order__id', 'used_date', 'is_paid_for', 'is_confirmed')
    list_editable = ('maintenance', 'order', 'comment', 'is_paid_for', 'is_confirmed')

class OrderAdmin(admin.ModelAdmin):
    # form = CategoryAdminForm
    list_display = ('id', 'room', 'registration_date', 'id_client', 'is_paid_for', 'is_confirmed', 'living_start_date', 'living_finish_date', 'comment')
    list_display_links = ('id',)
    search_fields = ('id', 'room__room_number', 'id_client__id', 'living_start_date', 'living_finish_date',)
    list_editable = ('is_paid_for', 'is_confirmed')

class BlockAdmin(admin.ModelAdmin):
    list_display = ('block_id', 'room', 'block_start_date', 'block_finish_date', 'reason')
    list_display_links = ('block_id',)
    search_fields = ('block_id', 'room__id')
    list_editable = ('room', 'block_start_date', 'block_finish_date', 'reason')

admin.site.register(MaintenanceOrders, MaintenanceOrdersAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(RoomType, RoomTypeAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Block, BlockAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Maintenance, MaintenanceAdmin)