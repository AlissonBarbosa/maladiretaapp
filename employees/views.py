from django.shortcuts import render

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse

from .models import Employee
from .forms import EmployeeForm

def export_telegrama(request):
        query = request.session.get("query_filter")
        if query:
            content = [ "{}#Sr(a)#{}#{}#{}#{}#{}#{}#{}#Brasil#######\n".format(employee.name,
                        employee.name, employee.street,
                        employee.neighborhood, employee.number,
                        employee.city, employee.state,
                        employee.cep.replace('.','').replace('-',''))
                        for employee in Employee.objects.search(query)]
        else:
            content = [ "{}#Sr(a)#{}#{}#{}#{}#{}#{}#{}#Brasil#######\n".format(employee.name,
                        employee.name, employee.street,
                        employee.neighborhood, employee.number,
                        employee.city, employee.state,
                        employee.cep.replace('.','').replace('-',''))
                        for employee in Employee.objects.all() ]

        filename = "telegrama_funcionarios.txt"
        response = HttpResponse(content, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
        return response

class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = Employee
    success_url = reverse_lazy('employees:funcionarios')
    form_class = EmployeeForm

    def form_valid(self, form):
        super(EmployeeCreateView, self).form_valid(form)
        messages.success(self.request, 'Funcionário criado com sucesso!')
        return HttpResponseRedirect(self.get_success_url())

class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = Employee

class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = Employee
    success_url = reverse_lazy('employees:funcionarios')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Funcionário excluído com sucesso!')
        return super(EmployeeDeleteView, self).delete(request, *args, **kwargs)

class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
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
            context = Employee.objects.search(filter_value)
            self.request.session['query_filter'] = filter_value
        else:
            context = Employee.objects.all()
            self.request.session['query_filter'] = None
        return context

class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = Employee
    success_url = reverse_lazy('employees:funcionarios')
    template_name = "employees/employee_update_form.html"
    form_class = EmployeeForm

    def form_valid(self, form):
        super(EmployeeUpdateView, self).form_valid(form)
        messages.success(self.request, 'Funcionário atualizado com sucesso!')
        return HttpResponseRedirect(self.get_success_url())