from django.urls import path

from .views import InstitutionCreateView, InstitutionDeleteView, InstitutionDetailView, InstitutionListView, InstitutionUpdateView

app_name = 'institutions'
urlpatterns = [
    path('', InstitutionListView.as_view(), name='instituicoes'),
    path('cadastrar/', InstitutionCreateView.as_view(), name='cadastrar'),
    path('<int:pk>', InstitutionDetailView.as_view(), name='instituicao'),
    path('excluir/<int:pk>', InstitutionDeleteView.as_view(), name='excluir'),
    path('editar/<int:pk>', InstitutionUpdateView.as_view(), name='editar'),
]