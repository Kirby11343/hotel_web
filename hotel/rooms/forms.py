from django import forms
from .models import *

class RoomTypeAdminForm(forms.ModelForm):
    class Meta:
        model = RoomType
        widgets = {
            'content': forms.Textarea
        }
        fields = '__all__'


class CategoryAdminForm(forms.ModelForm):
    class Meta:
        model = Category
        widgets = {
            'category_description': forms.Textarea
        }
        fields = '__all__'