from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy

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

class MaintenanceOrderCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = MaintenanceOrders
    template_name = 'maintenance/maintenance_create.html'
    context_object_name = 'maintenance_orders'
    fields = ('maintenance', 'order', 'comment',)
    success_message = "Замовлення було створено. Подивитися замовлення можливо у особистому кабінеті."
    success_url = reverse_lazy('main')

    def get_context_data(self, *args, **kwargs):
        context = super(MaintenanceOrderCreateView, self).get_context_data(*args, **kwargs)
        context['orders'] = Order.objects.all()
        return context

    def form_valid(self, form):
        morder = form.save(commit=False)
        morder.is_paid_for = False
        morder.is_confirmed = False
        morder.used_date = date.today()
        return super(MaintenanceOrderCreateView, self).form_valid(form)

class MaintenanceOrderDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = MaintenanceOrders
    template_name = 'order/order_confirm_delete.html'
    success_message = "Додаткове замовлення було видалено."
    success_url = reverse_lazy('main')

class RoomTypeDetailView(LoginRequiredMixin, DetailView):
    model = RoomType
    template_name = 'room/room_type_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(RoomTypeDetailView, self).get_context_data(*args, **kwargs)
        context['rooms'] = Room.objects.all().filter(price__room_type_fk=self.object)
        return context

def room_date_range_view(request):
    d1 = request.POST.get("search_living_start_date")
    d2 = request.POST.get("search_living_finish_date")
    free_rooms = do_request(f"SELECT * FROM show_free_rooms('{d1}', '{d2}')")
    context = {
        "free_rooms": free_rooms,
        "d1": d1,
        "d2": d2,
    }
    return render(request, "room/rooms_filter.html", context)

class OrderCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Order
    form_class = CreateOrderForm
    template_name = 'order/create_order.html'
    success_message = "Замовлення було створено. Подивитися замовлення можливо у особистому кабінеті."
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        order = form.save(commit=False)
        order.id_client = self.request.user
        return super(OrderCreateView, self).form_valid(form)

class OrderDetailView(SuccessMessageMixin, LoginRequiredMixin, DetailView):
    model = Order
    context_object_name = 'order'
    # form_class = CreateOrderForm
    template_name = 'order/detail_order.html'

    def get_context_data(self, *args, **kwargs):
        context = super(OrderDetailView, self).get_context_data(*args, **kwargs)
        context['morders'] = MaintenanceOrders.objects.all().filter(order_id=self.object)
        return context


class OrderDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Order
    template_name = 'order/order_confirm_delete.html'
    success_message = "Замовлення було видалено."
    success_url = reverse_lazy('main')

