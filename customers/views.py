from django.shortcuts import render

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.http import HttpResponseRedirect

from .models import Customer
from .forms import CustomerForm

class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    success_url = reverse_lazy('customers:clientes')
    form_class = CustomerForm

    def form_valid(self, form):
        super(CustomerCreateView, self).form_valid(form)
        messages.success(self.request, 'Cliente criado com sucesso!')
        return HttpResponseRedirect(self.get_success_url())

class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer

class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    success_url = reverse_lazy('customers:clientes')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Cliente excluído com sucesso!')
        return super(CustomerDeleteView, self).delete(request, *args, **kwargs)

class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    paginate_by = 25

    def get_queryset(self):
        filter_value = self.request.GET.get('filter')
        if filter_value:
            context = Customer.objects.search(filter_value)
        else:
            context = Customer.objects.all()
        return context

class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    success_url = reverse_lazy('customers:clientes')
    template_name = 'customers/customer_update_form.html'
    form_class = CustomerForm

    def form_valid(self, form):
        super(CustomerUpdateView, self).form_valid(form)
        messages.success(self.request, 'Cliente atualizado com sucesso!')
        return HttpResponseRedirect(self.get_success_url())
