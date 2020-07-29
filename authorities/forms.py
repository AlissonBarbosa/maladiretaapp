from django import forms
from .models import Authoritie

class AuthoritieForm(forms.ModelForm):
    class Meta:
        model = Authoritie
        fields = ['name', 'birth', 'position', 'institution']
        labels = {
            'name': 'Nome',
            'created': 'Criado em',
            'birth': 'Data de Nascimento',
            'position': 'Cargo',
            'institution': 'Instituição'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'birth': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':"form-control cc-name valid", 'type':'date'}),
            'position': forms.Select(attrs={'class':"form-control cc-name valid"}),
            'institution': forms.Select(attrs={'class':"form-control cc-name valid"})
        }