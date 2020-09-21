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
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not context.get('is_paginated', False):
            return context
        
        paginator = context.get('paginator')
        num_pages = paginator.num_pages
        current_page = context.get('page_obj')
        page_no = current_page.number
        

        if num_pages <= 11 or page_no <= 6:
            pages = [x for x in range(1, min(num_pages + 1, 12))]
        elif page_no > num_pages - 6:
            pages = [x for x in range(num_pages - 10, num_pages + 1)]
        else:
            pages = [x for x in range(page_no - 5, page_no + 6)]
        

        context.update({'pages': pages, 'previous_page': pages[0], 'next_page': pages[-1]})
        return context

    def get_queryset(self):
        filter_value = self.request.GET.get('filter')
        self.request.session['query_origin'] = 'Candidate'
        if filter_value:
            context = Candidate.objects.search(filter_value)
            self.request.session['query_filter'] = filter_value
        else:
            context = Candidate.objects.all()
            self.request.session['query_filter'] = None
        return context

class CandidateUpdateView(LoginRequiredMixin, UpdateView):
    model = Candidate
    success_url = reverse_lazy('candidates:candidatos')
    template_name = 'candidates/candidate_update_form.html'
    form_class = CandidateForm

    def form_valid(self, form):
        super(CandidateUpdateView, self).form_valid(form)
        messages.success(self.request, 'Candidato atualizado com sucesso!')
        return HttpResponseRedirect(self.get_success_url())
