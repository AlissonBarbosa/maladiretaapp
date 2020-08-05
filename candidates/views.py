from django.shortcuts import render

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.http import HttpResponseRedirect

from .models import Candidate
from .forms import CandidateForm

class CandidateCreateView(LoginRequiredMixin, CreateView):
    model = Candidate
    success_url = reverse_lazy('candidates:candidatos')
    form_class = CandidateForm

    def form_valid(self, form):
        super(CandidateCreateView, self).form_valid(form)
        messages.success(self.request, 'Candidato criado com sucesso!')
        return HttpResponseRedirect(self.get_success_url())

class CandidateDetailView(LoginRequiredMixin, DetailView):
    model = Candidate

class CandidateDeleteView(LoginRequiredMixin, DeleteView):
    model = Candidate
    success_url = reverse_lazy('candidates:candidatos')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Candidato excluído com sucesso!')
        return super(CandidateDeleteView, self).delete(request, *args, **kwargs)

class CandidateListView(LoginRequiredMixin, ListView):
    model = Candidate
    paginate_by = 25

    def get_queryset(self):
        filter_value = self.request.GET.get('filter')
        if filter_value:
            context = Candidate.objects.search(filter_value)
        else:
            context = Candidate.objects.all()
        return context

class CandidateUpdateView(LoginRequiredMixin, UpdateView):
    model = Candidate
    success_url = reverse_lazy('candidates:candidatos')
    form_class = CandidateForm

    def form_valid(self, form):
        super(CandidateUpdateView, self).form_valid(form)
        messages.success(self.request, 'Candidato atualizado com sucesso!')
        return HttpResponseRedirect(self.get_success_url())
