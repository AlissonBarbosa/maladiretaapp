from django import forms
from .models import Institution

class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = ['name', 'phone_number', 'city', 'street', 'number', 'complement', 'cep', 'state']
        labels = {
            'name': 'Nome',
            'phone_number': 'Telefone',
            'city': 'Cidade',
            'street': 'Rua',
            'number': 'Número',
            'complement': 'Complemento',
            'cep': 'CEP',
            'state': 'Estado'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'phone_number': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'city': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'street': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'number': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'complement': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'cep': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'state': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'})
        }