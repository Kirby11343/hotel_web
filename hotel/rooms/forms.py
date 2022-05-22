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

class CreateOrderForm(forms.ModelForm):
    living_start_date = forms.DateField(label='Дата заїзду', widget=forms.DateInput(attrs={'type': 'date'}))
    living_finish_date = forms.DateField(label='Дата виїзду', widget=forms.DateInput(attrs={'type': 'date'}))
    comment = forms.CharField(label='Коментарій', widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Order
        fields = '__all__'

    def save(self, commit=True):
        print("CHEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEECK")
        order = super(CreateOrderForm, self).save(commit=False)
        user = order.client.username
        order.client.id = user
        print("CHEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEECK")
        print(order.client)
        print(order.client.id)
        print(order.client.username)
        if commit:
            order.save()