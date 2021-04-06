from django import forms
from .models import Position

class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['position', 'handling', 'abbreviation']
        labels = {
            'position' : "Nome",
            'handling' : "Tratamento",
            'abbreviation' : "Abreviatura"
        }
        widgets = {
            'position' : forms.TextInput(attrs={'class':"form-control valid", 'autocomplete': 'off'}),
            'handling' : forms.TextInput(attrs={'class':"form-control valid", 'autocomplete': 'off',}),
            'abbreviation' : forms.TextInput(attrs={'class':"form-control valid", 'autocomplete': 'off',})
        }
        error_messages = {
            'position' : {
                'required': 'Nome é um campo obrigatorio'
            },
            'handling' : {
                'required': 'Tratamento é um campo obrigatorio'
            },
            'abbreviation': {
                'required': 'Abreviação é um campo obrigatorio'
            }
        }