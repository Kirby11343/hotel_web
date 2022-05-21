from django.contrib import admin
from .forms import *

class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm
    list_display = ('category_title', 'category_description',)
    list_display_links = ('category_title',)
    search_fields = ('category_title',)
    list_editable = ('category_description',)

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

admin.site.register(Order)
admin.site.register(Room)
admin.site.register(RoomType, RoomTypeAdmin)
admin.site.register(Price)
admin.site.register(Block)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Maintenance, MaintenanceAdmin)