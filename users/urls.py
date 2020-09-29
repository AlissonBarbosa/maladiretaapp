from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import MyAuthenticationForm, MyPasswordChangeForm
from django.urls import reverse_lazy

app_name = 'usuarios'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(form_class=MyAuthenticationForm, template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('mudar-senha/', auth_views.PasswordChangeView.as_view(form_class=MyPasswordChangeForm, template_name='registration/change-password.html', success_url='/'), name='change-password')
]