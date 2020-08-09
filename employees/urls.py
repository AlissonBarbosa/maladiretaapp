from django.urls import path
from .views import EmployeeCreateView, EmployeeDetailView, EmployeeDeleteView, EmployeeListView, EmployeeUpdateView

app_name = 'employees'
urlpatterns = [
    path('', EmployeeListView.as_view(), name='funcionarios'),
    path('cadastrar/', EmployeeCreateView.as_view(), name='cadastrar'),
    path('<int:pk>', EmployeeDetailView.as_view(), name='funcionario'),
    path('excluir/<int:pk>', EmployeeDeleteView.as_view(), name='excluir'),
    path('editar/<int:pk>', EmployeeUpdateView.as_view(), name='editar'),
]