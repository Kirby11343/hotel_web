from django.contrib import admin
from .models import *

# Register your models here.

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'room_type_title', 'room_number', 'category_title', 'maintenance_title', 'room_image', 'thumbnail_preview')
    list_display_links = ('id',)
    search_fields = ('id',)
    list_editable = ('room_type_title', 'room_number', 'category_title', 'maintenance_title', 'room_image')
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Мініатюра'
    thumbnail_preview.allow_tags = True


admin.site.register(Room)
admin.site.register(RoomType)
admin.site.register(Rate)
admin.site.register(Price)
admin.site.register(Block)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Category)
admin.site.register(Maintenance)