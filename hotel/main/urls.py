from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', UserView.as_view(), name="main"),
    path('cabinet/<int:pk>/', UserDetailView.as_view(), name="cabinet"),
    path('cabinet/update/<int:pk>/', UserUpdateView.as_view(), name="cabinet_update"),
    path("register", register_request, name="register"),
    path("login", login_request, name="login"),
    path("logout", logout_request, name="logout"),

    path("contacts", contacts_request, name="contacts"),

    path("create_review", CreateReviewView.as_view(), name="create_review"),
    path("detail_review/<int:pk>", DetailReviewView.as_view(), name="detail_review"),
    path("update_review/<int:pk>", UpdateReviewView.as_view(), name="update_review"),
    path("review/<int:pk>/delete", DeleteReviewView.as_view(), name="delete_review"),

    path('accounts/', include('allauth.urls')),

    path("password_reset", password_reset_request, name="password_reset"),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='main/password/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="main/password/password_reset_confirm.html"),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='main/password/password_reset_complete.html'),
         name='password_reset_complete'),
]