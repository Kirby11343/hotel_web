from django.db.models import Model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import NewUserForm, UserLoginForm, CustomPasswordResetFrom, CreateReviewForm
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.core.mail import send_mail, BadHeaderError
from hotel.settings import EMAIL_HOST_USER
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *

def contacts_request(request):

	return render (request=request, template_name="main/contacts.html")

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
	template_name = 'main/main.html'
	model = AuthUser
	context_object_name = 'user_list'
	def get_context_data(self, **kwargs):
		context = super(UserView, self).get_context_data(**kwargs)
		context.update({
			'review_list': Reviews.objects.order_by('id'),
		})
		return context

	def get_queryset(self):
		return Reviews.objects.order_by('id')

class CreateReviewView(LoginRequiredMixin, CreateView):
	form_class = CreateReviewForm
	model = Reviews
	template_name = 'main/review/create_review.html'
	success_url = "/"

class DetailReviewView(LoginRequiredMixin, DetailView):
	model = Reviews
	template_name = 'main/review/detail_review.html'

class UpdateReviewView(LoginRequiredMixin, UpdateView):
	form_class = CreateReviewForm
	model = Reviews
	template_name = 'main/review/update_review.html'

class DeleteReviewView(LoginRequiredMixin, DeleteView):
	model = Reviews
	success_url = reverse_lazy('main')





