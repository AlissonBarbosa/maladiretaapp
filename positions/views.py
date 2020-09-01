from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Position
from .forms import PositionForm
from django.contrib import messages
from django.http import HttpResponseRedirect

class PositionCreateView(LoginRequiredMixin, CreateView):
    model = Position
    form_class = PositionForm
    success_url = reverse_lazy('positions:cargos')

    def form_valid(self,form):
        super(PositionCreateView,self).form_valid(form)
        messages.success(self.request, 'Cargo criado com sucesso!')        
        return HttpResponseRedirect(self.get_success_url())

class PositionListView(LoginRequiredMixin, ListView):
    model = Position
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
            context = Position.objects.search(filter_value)
            self.paginate_by = len(context)
        else:
            context = Position.objects.all()
        return context
    
class PositionDetailView(LoginRequiredMixin, DetailView):
    model = Position

class PositionDeleteView(LoginRequiredMixin, DeleteView):
    model = Position
    success_url = reverse_lazy('positions:cargos')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Cargo excluído com sucesso!')
        return super(PositionDeleteView, self).delete(request, *args, **kwargs)

class PositionUpdateView(LoginRequiredMixin, UpdateView):
    model = Position
    form_class = PositionForm
    template_name = 'positions/position_update_form.html'
    success_url = reverse_lazy('positions:cargos')

    def form_valid(self,form):
        super(PositionUpdateView,self).form_valid(form)
        messages.success(self.request, 'Cargo atualizado com sucesso!')        
        return HttpResponseRedirect(self.get_success_url())