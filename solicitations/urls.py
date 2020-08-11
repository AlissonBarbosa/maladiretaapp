from django.urls import path
from .views import SolicitationCreateView, SolicitationDeleteView, SolicitationDetailView, SolicitationListView, SolicitationUpdateView

app_name = 'solicitations'
urlpatterns = [
    path('', SolicitationListView.as_view(), name='pleitos'),
    path('cadastrar/', SolicitationCreateView.as_view(), name='cadastrar'),
    path('<int:pk>', SolicitationDetailView.as_view(), name='pleito'),
    path('excluir/<int:pk>', SolicitationDeleteView.as_view(), name='excluir'),
    path('editar/<int:pk>', SolicitationUpdateView.as_view(), name='editar'),
]