from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm


from .models import *

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			form.save()
			# login(request, user)
			messages.success(request, "Реєстрація успішна." )
			return redirect('login')
		else:
			messages.error(request, "Невдала реєстрація. Недійсна інформація.")
	else:
		form = NewUserForm()
	return render (request=request, template_name="main/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})

class UserView(ListView):
    model = AuthUser
    template_name = 'main/main.html'
    # context_object_name = 'qwe'
    # extra_context = 'qwe'


