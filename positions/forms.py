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
            'position' : forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'handling' : forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off',}),
            'abbreviation' : forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off',})
        }