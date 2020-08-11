from django.shortcuts import render

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.http import HttpResponseRedirect

from .models import Solicitation
from .forms import SolicitationForm

class SolicitationCreateView(LoginRequiredMixin, CreateView):
    model = Solicitation
    success_url = reverse_lazy('solicitations:pleitos')
    form_class = SolicitationForm

    def form_valid(self, form):
        super(SolicitationCreateView, self).form_valid(form)
        messages.success(self.request, 'Pleito criado com sucesso!')
        return HttpResponseRedirect(self.get_success_url())

class SolicitationDetailView(LoginRequiredMixin, DetailView):
    model = Solicitation

class SolicitationDeleteView(LoginRequiredMixin, DeleteView):
    model = Solicitation
    success_url = reverse_lazy('solicitations:pleitos')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Pleito excluído com sucesso!')
        return super(SolicitationDeleteView, self).delete(request, *args, **kwargs)

class SolicitationListView(LoginRequiredMixin, ListView):
    model = Solicitation
    paginate_by = 25

    def get_queryset(self):
        filter_value = self.request.GET.get('filter')
        if filter_value:
            context = Solicitation.objects.search(filter_value)
        else:
            context = Solicitation.objects.all()
        return context

class SolicitationUpdateView(LoginRequiredMixin, UpdateView):
    model = Solicitation
    success_url = reverse_lazy('solicitations:pleitos')
    template_name = "solicitations/solicitation_update_form.html"
    form_class = SolicitationForm

    def form_valid(self, form):
        super(SolicitationUpdateView, self).form_valid(form)
        messages.success(self.request, 'Pleito atualizado com sucesso!')
        return HttpResponseRedirect(self.get_success_url())