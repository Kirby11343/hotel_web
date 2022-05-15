from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import NewUserForm, UserLoginForm, CustomPasswordResetFrom
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.core.mail import send_mail, BadHeaderError
from hotel.settings import EMAIL_HOST_USER

from .models import *

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = CustomPasswordResetFrom(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = AuthUser.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "main/password/password_reset_email.txt"
					c = {
						"email":user.email,
						'domain':'127.0.0.1:8000',
						'site_name': 'Hotel Odessa',
						"uid": urlsafe_base64_encode(force_bytes(user.pk)),
						"user": user,
						'token': default_token_generator.make_token(user),
						'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, EMAIL_HOST_USER, [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Знайдено недійсний заголовок.')
					messages.success(request, 'Повідомлення з інструкціями щодо відновлення пароля було надіслано на вашу папку "Вхідні".')
					return redirect ("/password_reset/done/")
			messages.error(request, 'Введено недійсну адресу електронної пошти.')
	password_reset_form = CustomPasswordResetFrom()
	return render(request=request, template_name="main/password/password_reset.html", context={"password_reset_form":password_reset_form})

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Реєстрація успішна." )
			return redirect('login')
		else:
			messages.error(request, "Невдала реєстрація. Недійсна інформація.")
	else:
		form = NewUserForm()
	return render (request=request, template_name="main/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = UserLoginForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"Тепер ви ввійшли як {username}.")
				return redirect("main")
			else:
				messages.error(request,"Неправильне ім'я користувача або пароль.")
		else:
			messages.error(request,"Неправильне ім'я користувача або пароль.")
	form = UserLoginForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.success(request, "Ви більше не авторизовані.")
	return redirect('main')

class UserView(ListView):
    model = AuthUser
    template_name = 'main/main.html'
    # context_object_name = 'qwe'
    # extra_context = 'qwe'


