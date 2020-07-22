from django import forms
from django.contrib.auth.forms import AuthenticationForm

class MyAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Usuário', widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class':"au-input au-input--full"}))