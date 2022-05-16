from django.shortcuts import render
from .models import Gallery
from django.views.generic import ListView, DetailView, CreateView, DeleteView

# Create your views here.

class GalleryListView(ListView):
    model = Gallery
    template_name = 'gallery/gallery.html'
    paginate_by = 4