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
                        for authoritie in Authoritie.objects.search(query)]
        else:
            content = [ "{}#Sr(a)#{}#{}#{}#{}#{}#{}#{}#Brasil#######\n".format(authoritie.name,
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
