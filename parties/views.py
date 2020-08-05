from django.shortcuts import render

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.http import HttpResponseRedirect

from .models import Party
from .forms import PartyForm

class PartyCreateView(LoginRequiredMixin, CreateView):
    model = Party
    success_url = reverse_lazy('parties:partidos')
    form_class = PartyForm

    def form_valid(self, form):
        super(PartyCreateView, self).form_valid(form)
        messages.success(self.request, 'Partido criado com sucesso!')
        return HttpResponseRedirect(self.get_success_url())

class PartyDetailView(LoginRequiredMixin, DetailView):
    model = Party

class PartyDeleteView(LoginRequiredMixin, DeleteView):
    model = Party
    success_url = reverse_lazy('parties:partidos')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Partido excluído com sucesso!')
        return super(PartyDeleteView, self).delete(request, *args, **kwargs)

class PartyListView(LoginRequiredMixin, ListView):
    model = Party
    paginate_by = 25

    def get_queryset(self):
        filter_value = self.request.GET.get('filter')
        if filter_value:
            context = Party.objects.search(filter_value)
        else:
            context = Party.objects.all()
        return context

class PartyUpdateView(LoginRequiredMixin, UpdateView):
    model = Party
    form_class = PartyForm
    template_name = 'parties/party_update_form.html'
    success_url = reverse_lazy('parties:partidos')

    def form_valid(self, form):
        super(PartyUpdateView, self).form_valid(form)
        messages.success(self.request, 'Partido atualizado com sucesso!')
        return HttpResponseRedirect(self.get_success_url())