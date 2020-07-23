from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Position
from .forms import PositionForm

class PositionCreateView(LoginRequiredMixin,CreateView):
    model = Position
    form_class = PositionForm

class PositionListView(LoginRequiredMixin, ListView):
    model = Position
    paginate_by = 10

    def get_queryset(self):
        filter_value = self.request.GET.get('filter')
        if filter_value:
            context = Position.objects.filter(position = filter_value)
        else:
            context = Position.objects.all()
        return context
    
class PositionDetailView(LoginRequiredMixin, DetailView):
    model = Position

class PositionDeleteView(LoginRequiredMixin, DeleteView):
    model = Position
    success_url = reverse_lazy('positions:cargos')

class PositionUpdateView(LoginRequiredMixin, UpdateView):
    model = Position
    form_class = PositionForm
    template_name = 'positions/position_update_form.html'