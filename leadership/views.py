from django.shortcuts import render

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.http import HttpResponseRedirect

from .models import Leadership
from .forms import LeadershipForm

class LeadershipCreateView(LoginRequiredMixin, CreateView):
    model = Leadership
    form_class = LeadershipForm
    success_url = reverse_lazy('leadership:liderancas')

    def form_valid(self,form):
        super(LeadershipCreateView,self).form_valid(form)
        messages.success(self.request, 'Liderança criada com sucesso!')
        return HttpResponseRedirect(self.get_success_url())

class LeadershipDetailView(LoginRequiredMixin, DetailView):
    model = Leadership

class LeadershipDeleteView(LoginRequiredMixin, DeleteView):
    model = Leadership
    success_url = reverse_lazy('leadership:liderancas')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Liderança excluída com sucesso!')
        return super(LeadershipDeleteView, self).delete(request, *args, **kwargs)

class LeadershipListView(LoginRequiredMixin, ListView):
    model = Leadership
    paginate_by = 25

    def get_queryset(self):
        filter_value = self.request.GET.get('filter')
        if filter_value:
            context = Leadership.objects.search(filter_value)
        else:
            context = Leadership.objects.all()
        return context

class LeadershipUpdateView(LoginRequiredMixin, UpdateView):
    model = Leadership
    form_class = LeadershipForm
    template_name = 'leadership/leadership_update_form.html'
    success_url = reverse_lazy('leadership:liderancas')

    def form_valid(self,form):
        super(LeadershipUpdateView,self).form_valid(form)
        messages.success(self.request, 'Liderança atualizada com sucesso!')
        return HttpResponseRedirect(self.get_success_url())
        