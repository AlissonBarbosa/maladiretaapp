from django.shortcuts import render

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Institution
from .forms import InstitutionForm

class InstitutionCreateView(LoginRequiredMixin,CreateView):
    model = Institution
    form_class = InstitutionForm

class InstitutionDetailView(LoginRequiredMixin, DetailView):
    model = Institution

class InstitutionDeleteView(LoginRequiredMixin, DeleteView):
    model = Institution
    success_url = reverse_lazy('institutions:instituicoes')

class InstitutionListView(LoginRequiredMixin, ListView):
    model = Institution
    paginate_by = 10

    def get_queryset(self):
        filter_value = self.request.GET.get('filter')
        if filter_value:
            context = Institution.objects.filter(position = filter_value)
        else:
            context = Institution.objects.all()
        return context

class InstitutionUpdateView(LoginRequiredMixin, UpdateView):
    model = Institution
    form_class = InstitutionForm
    template_name = 'institutions/institution_update_form.html'
