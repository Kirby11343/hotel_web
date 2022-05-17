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
        # widgets = {
        #     'category_description': forms.Textarea
        # }
        fields = '__all__'