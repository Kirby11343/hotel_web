from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404

from .forms import CreateOrderForm
from .models import *
from django.views.generic import ListView, DetailView, CreateView, DeleteView


# Create your views here.

class GalleryListView(ListView):
    model = Gallery
    template_name = 'gallery/gallery.html'
    paginate_by = 18

class RoomTypeListView(ListView):
    model = RoomType
    template_name = 'room/room_type.html'

class CategoryListView(ListView):
    model = Category
    template_name = 'category/category.html'

    # def get_queryset(self):
    #     category_title = self.kwargs['category_title']
    #     return Category.objects.filter(category_title=category_title)

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category/category_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(*args, **kwargs)
        context['maintenances'] = Maintenance.objects.all().filter(category=self.object)
        return context

class RoomTypeDetailView(DetailView):
    model = RoomType
    template_name = 'room/room_type_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(RoomTypeDetailView, self).get_context_data(*args, **kwargs)
        context['rooms'] = Room.objects.all().filter(room_type=self.object)
        return context

class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = CreateOrderForm
    # fields = ('maintenance', 'room', 'client', 'living_start_date', 'living_finish_date', 'comment')
    template_name = 'order/create_order.html'