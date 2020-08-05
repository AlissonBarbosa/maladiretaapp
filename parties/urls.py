from django.urls import path
from .views import PartyCreateView, PartyDeleteView, PartyDetailView, PartyListView, PartyUpdateView

app_name = 'parties'

urlpatterns = [
    path('', PartyListView.as_view(), name='partidos'),
    path('cadastrar/', PartyCreateView.as_view(), name='cadastrar'),
    path('<int:pk>', PartyDetailView.as_view(), name='partido'),
    path('excluir/<int:pk>', PartyDeleteView.as_view(), name='excluir'),
    path('editar/<int:pk>', PartyUpdateView.as_view(), name='editar'),
]