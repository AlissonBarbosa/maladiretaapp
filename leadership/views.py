from django.shortcuts import render

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse

from .models import Leadership
from  positions.models import Position
from .forms import LeadershipForm

def export_telegrama(request):
        query = request.session.get("query_filter")
        if query:
            content = []
            for leadership in Leadership.objects.search(query):
                abbreviation = "Sr(a)"
                if leadership.position:
                    abbreviation = Position.objects.search(leadership.position)[0].abbreviation
                content.append("{}#{}#{}#{}#{}#{}#{}#{}#{}#Brasil#######\n".format(leadership.name, abbreviation.replace("\n",''),
                        leadership.name, leadership.street,
                        leadership.neighborhood, leadership.number,
                        leadership.city, leadership.state,
                        leadership.cep.replace('.','').replace('-','')))
        else:
            content = []
            for leadership in Leadership.objects.all():
                abbreviation = "Sr(a)"
                if leadership.position:
                    abbreviation = Position.objects.search(leadership.position)[0].abbreviation
                content.append("{}#{}#{}#{}#{}#{}#{}#{}#{}#Brasil#######\n".format(leadership.name, abbreviation.replace("\n",''),
                        leadership.name, leadership.street,
                        leadership.neighborhood, leadership.number,
                        leadership.city, leadership.state,
                        leadership.cep.replace('.','').replace('-','')))

        filename = "telegrama_lideranças.txt"
        response = HttpResponse(content, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
        return response

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
        self.request.session['query_origin'] = 'Leadership'
        if filter_value:
            context = Leadership.objects.search(filter_value)
            self.request.session['query_filter'] = filter_value
        else:
            context = Leadership.objects.all()
            self.request.session['query_filter'] = None
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
        