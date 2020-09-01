from django.shortcuts import render

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse

from .models import Authoritie
from .forms import AuthoritieForm

def export_telegrama(request):
        query = request.session.get("query_filter")
        if query:
            content = [ "{}#Sr(a)#{}#{}#{}#{}#{}#{}#{}#Brasil#######\n".format(authoritie.name,
                        authoritie.name, authoritie.institution.street,
                        authoritie.institution.neighborhood, authoritie.institution.number,
                        authoritie.institution.city, authoritie.institution.state,
                        authoritie.institution.cep.replace('.','').replace('-',''))
                        if not authoritie.position.abbreviation else
                        "{}#{}#{}#{}#{}#{}#{}#{}#{}#Brasil#######\n".format(authoritie.name,authoritie.position.abbreviation.replace("\n",''),
                        authoritie.name, authoritie.institution.street,
                        authoritie.institution.neighborhood, authoritie.institution.number,
                        authoritie.institution.city, authoritie.institution.state,
                        authoritie.institution.cep.replace('.','').replace('-',''))
                        for authoritie in Authoritie.objects.search(query)]
        else:
            content = [ "{}#Sr(a)#{}#{}#{}#{}#{}#{}#{}#Brasil#######\n".format(authoritie.name,
                        authoritie.name, authoritie.institution.street,
                        authoritie.institution.neighborhood, authoritie.institution.number,
                        authoritie.institution.city, authoritie.institution.state,
                        authoritie.institution.cep.replace('.','').replace('-',''))
                        if not authoritie.position.abbreviation else
                        "{}#{}#{}#{}#{}#{}#{}#{}#{}#Brasil#######\n".format(authoritie.name,authoritie.position.abbreviation.replace("\n",''),
                        authoritie.name, authoritie.institution.street,
                        authoritie.institution.neighborhood, authoritie.institution.number,
                        authoritie.institution.city, authoritie.institution.state,
                        authoritie.institution.cep.replace('.','').replace('-',''))
                        for authoritie in Authoritie.objects.all() ]

        filename = "telegrama_autoridades.txt"
        response = HttpResponse(content, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
        return response

class AuthoritieCreateView(LoginRequiredMixin, CreateView):
    model = Authoritie
    success_url = reverse_lazy('authorities:autoridades')
    form_class = AuthoritieForm

    def form_valid(self, form):
        super(AuthoritieCreateView, self).form_valid(form)
        messages.success(self.request, 'Autoridade criada com sucesso!')
        return HttpResponseRedirect(self.get_success_url())

class AuthoritieDetailView(LoginRequiredMixin, DetailView):
    model = Authoritie

class AuthoritieDeleteView(LoginRequiredMixin, DeleteView):
    model = Authoritie
    success_url = reverse_lazy('authorities:autoridades')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Autoridade excluída com sucesso!')
        return super(AuthoritieDeleteView, self).delete(request, *args, **kwargs)
    
class AuthoritieListView(LoginRequiredMixin, ListView):
    model = Authoritie
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
            context = Authoritie.objects.search(filter_value)
            self.request.session['query_filter'] = filter_value
        else:
            context = Authoritie.objects.all()
            self.request.session['query_filter'] = filter_value
        return context

class AuthoritieUpdateView(LoginRequiredMixin, UpdateView):
    model = Authoritie
    form_class = AuthoritieForm
    template_name = 'authorities/authoritie_update_form.html'
    success_url = reverse_lazy('authorities:autoridades')

    def form_valid(self,form):
        super(AuthoritieUpdateView,self).form_valid(form)
        messages.success(self.request, 'Autoridade atualizada com sucesso!')        
        return HttpResponseRedirect(self.get_success_url())
