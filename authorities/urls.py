from django.urls import path

from .views import AuthoritieCreateView, AuthoritieDeleteView, AuthoritieDetailView, AuthoritieListView, AuthoritieUpdateView

app_name = 'authorities'
urlpatterns = [
    path('', AuthoritieListView.as_view(), name='autoridades'),
    path('cadastrar/', AuthoritieCreateView.as_view(), name='cadastrar'),
    path('<int:pk>', AuthoritieDetailView.as_view(), name='autoridade'),
    path('excluir/<int:pk>', AuthoritieDeleteView.as_view(), name='excluir'),
    path('editar/<int:pk>', AuthoritieUpdateView.as_view(), name='editar'),
]