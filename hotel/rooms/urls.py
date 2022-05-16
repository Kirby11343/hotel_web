from django.urls import path, include
from .views import *

urlpatterns = [
    path('gallery/', GalleryListView.as_view(), name="gallery"),
]