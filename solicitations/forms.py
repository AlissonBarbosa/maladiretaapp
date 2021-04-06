from django import forms
from .models import Solicitation

SITUACAO = (
	('ABERTO', 'ABERTO'),
    ('ANDAMENTO', 'ANDAMENTO'),
	('CONCLUIDO', 'CONCLUIDO'),
    ('CANCELADO', 'CANCELADO')
	)

class SolicitationForm(forms.ModelForm):
    class Meta:
        model = Solicitation
        fields = '__all__'
        labels = {
            'created': 'Criado em',
            'updated': 'Atualizado em',
            'description': 'Descrição',
            'indication': 'Indicação', 
            'value': 'Valor', 
            'situation': 'Situação',
            'note': 'Observação',
            'customer': 'Cliente',
            'historic': 'Histórico'
        }
        widgets = {
            'created': forms.DateInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'updated': forms.DateInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'description': forms.Textarea(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'indication': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'value': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'situation': forms.Select(attrs={'class':"form-control cc-name valid"}, choices=SITUACAO),
            'note': forms.Textarea(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'historic': forms.Textarea(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'customer': forms.Select(attrs={'class':"form-control cc-name valid"})
        }
        error_messages = {
            'description': {
                'required': "Descrição é um campo obrigatório"
            },
            'customer': {
                'required': "Cliente é um campo obrigatório"
            }
        }
