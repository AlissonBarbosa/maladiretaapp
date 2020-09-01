from django.shortcuts import render

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.http import HttpResponseRedirect

from .models import Institution
from .forms import InstitutionForm

class InstitutionCreateView(LoginRequiredMixin,CreateView):
    model = Institution
    form_class = InstitutionForm
    success_url = reverse_lazy('institutions:instituicoes')

    def form_valid(self,form):
        super(InstitutionCreateView,self).form_valid(form)
        messages.success(self.request, 'Instituição criada com sucesso!')
        return HttpResponseRedirect(self.get_success_url())

class InstitutionDetailView(LoginRequiredMixin, DetailView):
    model = Institution

class InstitutionDeleteView(LoginRequiredMixin, DeleteView):
    model = Institution
    success_url = reverse_lazy('institutions:instituicoes')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Instituição excluída com sucesso!')
        return super(InstitutionDeleteView, self).delete(request, *args, **kwargs)

class InstitutionListView(LoginRequiredMixin, ListView):
    model = Institution
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
        if filter_value:
            context = Institution.objects.search(filter_value)
        else:
            context = Institution.objects.all()
        return context

class InstitutionUpdateView(LoginRequiredMixin, UpdateView):
    model = Institution
    form_class = InstitutionForm
    template_name = 'institutions/institution_update_form.html'
    success_url = reverse_lazy('institutions:instituicoes')

    def form_valid(self,form):
        super(InstitutionUpdateView,self).form_valid(form)
        messages.success(self.request, 'Instituição atualizada com sucesso!')        
        return HttpResponseRedirect(self.get_success_url())
