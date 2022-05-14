from django.urls import path
from .views import *

urlpatterns = [
    path('', UserView.as_view(), name="main"),
    path("register", register_request, name="register"),
    path("login", login_request, name="login"),
]