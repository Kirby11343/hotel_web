from django.shortcuts import render, get_object_or_404
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

class CategoryListView(ListView):
    model = Category
    template_name = 'category/category.html'

    # def get_queryset(self):
    #     category_title = self.kwargs['category_title']
    #     return Category.objects.filter(category_title=category_title)