from django.urls import path

from .views import PositionCreateView, PositionListView, PositionDetailView, PositionDeleteView, PositionUpdateView

app_name = 'positions'
urlpatterns = [
    path('', PositionListView.as_view(), name='cargos'),
    path('cadastrar/', PositionCreateView.as_view(), name='cadastrar'),
    path('<int:pk>', PositionDetailView.as_view(), name='cargo'),
    path('excluir/<int:pk>', PositionDeleteView.as_view(), name='excluir'),
    path('editar/<int:pk>', PositionUpdateView.as_view(), name='editar'),
]