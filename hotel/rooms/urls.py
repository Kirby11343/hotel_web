from django.urls import path, include
from .views import *

urlpatterns = [
    path('gallery/', GalleryListView.as_view(), name="gallery"),
    path('room_type/', RoomTypeListView.as_view(), name="room_type"),
    path('room_type_detail/<slug:slug>/', RoomTypeDetailView.as_view(), name="room_type_detail"),
    path('category/', CategoryListView.as_view(), name="category"),
    path('category_detail/<slug:slug>/', CategoryDetailView.as_view(), name="category_detail"),
    path('create_order/', OrderCreateView.as_view(), name="create_order"),
    path('rooms/', room_date_range_view, name="free_rooms"),
]

