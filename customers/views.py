from django.shortcuts import render

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse

from .models import Customer
from .forms import CustomerForm

def export_telegrama(request):
        query = request.session.get("query_filter")
        if query:
            content = [ "{}#Sr(a)#{}#{}#{}#{}#{}#{}#{}#Brasil#######\n".format(customer.name,
                        customer.name, customer.street,
                        customer.neighborhood, customer.number,
                        customer.city, customer.state,
                        customer.cep.replace('.','').replace('-',''))
                        for customer in Customer.objects.search(query)]
        else:
            content = [ "{}#Sr(a)#{}#{}#{}#{}#{}#{}#{}#Brasil#######\n".format(customer.name,
                        customer.name, customer.street,
                        customer.neighborhood, customer.number,
                        customer.city, customer.state,
                        customer.cep.replace('.','').replace('-',''))
                        for customer in Customer.objects.all() ]

        filename = "telegrama_clientes.txt"
        response = HttpResponse(content, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
        return response

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
            context = Customer.objects.search(filter_value)
            self.request.session['query_filter'] = filter_value
        else:
            context = Customer.objects.all()
            self.request.session['query_filter'] = None
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
