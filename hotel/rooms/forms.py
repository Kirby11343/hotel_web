from django import forms
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class RoomTypeAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(), label="Зміст")
    class Meta:
        model = RoomType
        # widgets = {
        #     'content': forms.Textarea
        # }
        fields = '__all__'


class CategoryAdminForm(forms.ModelForm):
    category_description = forms.CharField(widget=CKEditorUploadingWidget(), label="Опис категорії")
    class Meta:
        model = Category
        fields = '__all__'

class MaintenanceAdminForm(forms.ModelForm):
    maintenance_description = forms.CharField(widget=CKEditorUploadingWidget(), label="Опис послуги")
    class Meta:
        model = Maintenance
        fields = '__all__'