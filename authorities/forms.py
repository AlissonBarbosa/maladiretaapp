from django import forms
from .models import Authoritie

class AuthoritieForm(forms.ModelForm):
    class Meta:
        model = Authoritie
        fields = ['name', 'birth', 'email', 'phone_number', 'position', 'institution']
        labels = {
            'name': 'Nome',
            'created': 'Criado em',
            'birth': 'Nascimento',
            'phone_number': 'Telefone',
            'position': 'Cargo',
            'institution': 'Instituição'
        }
        localized_fields = ('birth',)
        widgets = {
            'name': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'birth': forms.DateInput(attrs={'class':"form-control cc-name valid", 'type':'text', 'autocomplete': 'off', 'data-mask':"00/00/0000"}),
            'email': forms.EmailInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'phone_number': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off', 'data-mask':"(00)00000-0000"}),
            'position': forms.Select(attrs={'class':"form-control cc-name valid"}),
            'institution': forms.Select(attrs={'class':"form-control cc-name valid"})
        }
        error_messages = {
            'name': {
                'required': "Nome é um campo obrigatório"
            }
        }