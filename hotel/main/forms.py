from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.http import request
from django.contrib.auth.models import AbstractUser
from django.shortcuts import redirect

from main.models import *
from datetime import datetime

class CreateReviewForm(forms.ModelForm):
	content = forms.CharField(label='Зміст', widget=forms.Textarea(attrs={'class': 'form-control'}))
	class Meta:
		model = Reviews
		fields = ('author', 'content',)
	def save(self, commit=True):
		review = super(CreateReviewForm, self).save(commit=False)
		if commit:
			review.save()
		return redirect('detail_review/<int:pk>')

class ReviewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(), label="Зміст")
    class Meta:
        model = Reviews
        # widgets = {
        #     'content': forms.Textarea
        # }
        fields = '__all__'


class CustomPasswordResetFrom(PasswordResetForm):
	email = forms.EmailField(label='Email адреса', widget=forms.EmailInput(attrs={'class': 'form-control'}))

class UserLoginForm(AuthenticationForm):
	username = forms.CharField(label='Ім\'я користувача', widget=forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class NewUserForm(UserCreationForm):
	password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))
	password2 = forms.CharField(label='Підтвердження пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

	class Meta:
		model = AuthUser
		fields = ("username", "email", "password1", "password2", "first_name", "last_name",)
		widgets = {
			'username': forms.TextInput(attrs={'class': 'form-control'}),
			'email': forms.EmailInput(attrs={'class': 'form-control'}),
			'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
			'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
			'first_name': forms.TextInput(attrs={'class': 'form-control'}),
			'last_name': forms.TextInput(attrs={'class': 'form-control'}),
		}

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.is_superuser = 0
		user.is_active = 1
		user.is_staff = 0
		user.date_joined = datetime.now()
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user