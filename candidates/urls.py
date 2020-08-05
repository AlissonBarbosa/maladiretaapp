from django.urls import path
from .views import CandidateCreateView, CandidateDetailView, CandidateDeleteView, CandidateListView, CandidateUpdateView

app_name = 'candidates'
urlpatterns = [
    path('', CandidateListView.as_view(), name='candidatos'),
    path('cadastrar/', CandidateCreateView.as_view(), name='cadastrar'),
    path('<int:pk>', CandidateDetailView.as_view(), name='candidato'),
    path('excluir/<int:pk>', CandidateDeleteView.as_view(), name='excluir'),
    path('editar/<int:pk>', CandidateUpdateView.as_view(), name='editar'),
]