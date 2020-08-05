from django import forms
from .models import Candidate

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'
        labels = {
            'name': 'Nome',
            'number': 'Número',
            'union': 'Coligação',
            'votes': 'Votos',
            'party': 'Partido',
            'position': 'Cargo'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'number': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'union': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'votes': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'party': forms.Select(attrs={'class':"form-control cc-name valid"}),
            'position': forms.Select(attrs={'class':"form-control cc-name valid"})
        }
        error_messages = {
            'name': {
                'required': "Nome é um campo obrigatório"
            },
            'number': {
                'required': "Número é um campo obrigatório"
            },
            'party': {
                'required': "Partido é um campo obrigatório"
            },
            'position': {
                'required': "Cargo é um campo obrigatório"
            },
        }