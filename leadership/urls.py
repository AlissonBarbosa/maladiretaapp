from django.urls import path
from .views import LeadershipCreateView, LeadershipDetailView, LeadershipDeleteView, LeadershipListView, LeadershipUpdateView, export_telegrama

app_name = 'leadership'
urlpatterns = [
    path('', LeadershipListView.as_view(), name='liderancas'),
    path('cadastrar/', LeadershipCreateView.as_view(), name='cadastrar'),
    path('<int:pk>', LeadershipDetailView.as_view(), name='lideranca'),
    path('excluir/<int:pk>', LeadershipDeleteView.as_view(), name='excluir'),
    path('editar/<int:pk>', LeadershipUpdateView.as_view(), name='editar'),
    path('download/', export_telegrama, name='download'),
]
