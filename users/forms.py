from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

class MyAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Usuário', widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class':"au-input au-input--full"}))

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Senha Antiga', widget=forms.PasswordInput(attrs={'class':"au-input au-input--full"}))
    new_password1 = forms.CharField(label='Nova Senha', widget=forms.PasswordInput(attrs={'class':"au-input au-input--full"}))
    new_password2 = forms.CharField(label='Confirmar Nova Senha', widget=forms.PasswordInput(attrs={'class':"au-input au-input--full"}))