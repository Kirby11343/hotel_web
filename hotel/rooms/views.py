from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render

from .forms import CreateOrderForm
from .models import *
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from .scripts import do_request


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

def room_date_range_view(request):
    free_rooms = do_request("SELECT * FROM show_free_rooms('2022-05-25', '2022-05-26')")
    context = {
        "free_rooms": free_rooms
    }
    return render(request, "room/room_type_detail.html", context)

class OrderCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Order
    form_class = CreateOrderForm
    template_name = 'order/create_order.html'
    success_message = "Замовлення було створено. Подивитися замовлення можливо у особистому кабінеті."
    success_url = '/'

    def form_valid(self, form):
        order = form.save(commit=False)
        order.id_client = self.request.user
        return super(OrderCreateView, self).form_valid(form)