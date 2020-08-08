from django.urls import path
from .views import CustomerCreateView, CustomerDeleteView, CustomerDetailView, CustomerListView, CustomerUpdateView

app_name = 'customers'
urlpatterns = [
    path('', CustomerListView.as_view(), name='clientes'),
    path('cadastrar/', CustomerCreateView.as_view(), name='cadastrar'),
    path('<int:pk>', CustomerDetailView.as_view(), name='cliente'),
    path('excluir/<int:pk>', CustomerDeleteView.as_view(), name='excluir'),
    path('editar/<int:pk>', CustomerUpdateView.as_view(), name='editar'),
]