from django import forms
from .models import Party

class PartyForm(forms.ModelForm):
    class Meta:
        model = Party
        fields = '__all__'
        labels = {
            'name': 'Nome',
            'initials': 'Sigla',
            'number': 'Número',
            'union': 'Coligação',
            'leadership': 'Presidente'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'initials': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'number': forms.NumberInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'union': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'leadership': forms.Select(attrs={'class':"form-control cc-name valid"})
        }
        error_messages = {
            'name': {
                'required': "Nome é um campo obrigatório"
            },
            'initials': {
                'required': "Sigla é um campo obrigatório"
            },
            'number': {
                'required': "Número é um campo obrigatório"
            },
            'leadership': {
                'required': "Presidente é um campo obrigatório"
            }
        }