from django.shortcuts import render

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.http import HttpResponseRedirect

from .models import Employee
from .forms import EmployeeForm

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
    paginate_by = 25

    def get_queryset(self):
        filter_value = self.request.GET.get('filter')
        if filter_value:
            context = Employee.objects.search(filter_value)
        else:
            context = Employee.objects.all()
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