from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, CreateView, DeleteView

# Create your views here.

class GalleryListView(ListView):
    model = Gallery
    template_name = 'gallery/gallery.html'
    paginate_by = 20


class RoomTypeListView(ListView):
    model = RoomType
    template_name = 'room/room_type.html'

    # def get_queryset(self):
    #     queryset = super(GalleryListView, self).get_queryset()
    #     queryset = queryset.annotate(num_apples=Count('tree__apple'), apple_mass=Sum('tree__apple__mass'))
    #     return queryset

class CategoryListView(ListView):
    model = Category
    template_name = 'category/category.html'