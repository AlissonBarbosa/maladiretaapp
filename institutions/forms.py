from django import forms
from .models import Institution

class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = '__all__'
        labels = {
            'name': 'Nome',
            'phone_number': 'Telefone',
            'city': 'Cidade',
            'street': 'Rua',
            'number': 'Número',
            'complement': 'Complemento',
            'cep': 'CEP',
            'state': 'Estado',
            'neighborhood': 'Bairro',
            'note': 'Observação'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'phone_number': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off', 'data-mask':"(00)0000-0000"}),
            'city': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'street': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'number': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'complement': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'cep': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off', 'data-mask':"00.000-000"}),
            'state': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'email': forms.EmailInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'note': forms.Textarea(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'neighborhood': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'})
        }
        error_messages = {
            'name': {
                'required': "Nome é um campo obrigatório"
            }
        }