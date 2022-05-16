from django.urls import path, include
from .views import *

urlpatterns = [
    path('gallery/', GalleryListView.as_view(), name="gallery"),
    path('room_type/', RoomTypeListView.as_view(), name="room_type"),
    path('category/', CategoryListView.as_view(), name="category"),
]