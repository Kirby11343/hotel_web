from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from .models import *

class UserView(ListView):
    model = AuthUser
    template_name = 'main/main.html'
    # context_object_name = 'qwe'
    # extra_context = 'qwe'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(UserView, self).get_context_data(**kwargs)
    #     context['title'] = 'Mainpage'
    #     return context

    # def get_queryset(self):
    #     return

# def mainpage(request):
#     users = AuthUser.objects.all()
#     phones = Phone.objects.all()
#     context = {
#         'users': users,
#         'phones': phones,
#     }
#     return render(request, 'main/main.html', context)

