from django import forms
from django.contrib.auth.forms import UserCreationForm
from main.models import AuthUser
from datetime import datetime


class NewUserForm(UserCreationForm):

	class Meta:
		model = AuthUser
		fields = ("username", "email", "password1", "password2", "first_name", "last_name",)

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.is_superuser = 0
		user.is_active = 1
		user.is_staff = 0
		user.date_joined = datetime.now()
		user.role = 'Користувач'
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user