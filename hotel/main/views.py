from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def mainpage(request):
    users = AuthUser.objects.all()
    phones = Phone.objects.all()
    context = {
        'users': users,
        'phones': phones,
    }
    return render(request, 'main/index.html', context)

