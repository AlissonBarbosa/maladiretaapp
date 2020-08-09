from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        labels = {
            'name': 'Nome',
            'birth': 'Nascimento',
            'nickname': 'Pseudonimo',
            'city': 'Cidade',
            'street': 'Rua',
            'number': 'Número',
            'complement': 'Complemento',
            'cep': 'CEP',
            'state': 'Estado',
            'neighborhood': 'Bairro',
            'phone_number': 'Telefone',
            'cellphone': 'Celular',
            'phone_home': 'Residencial',
            'function': 'Função',
            'note': 'Observação'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'birth': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'nickname': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'city': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'street': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'number': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'complement': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'cep': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off', 'data-mask':"00.000-000"}),
            'state': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'neighborhood': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'phone_number': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off', 'placeholder': '(xx)xxxx-xxxx', 'data-mask':"(00)0000-0000"}),
            'phone_home': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off', 'placeholder': '(xx)xxxx-xxxx', 'data-mask':"(00)0000-0000"}),
            'cellphone': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off', 'placeholder': '(xx)xxxxx-xxxx', 'data-mask':"(00)00000-0000"}),
            'function': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'email': forms.EmailInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'note': forms.Textarea(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'})
        }
        error_messages = {
            'name': {
                'required': "Nome é um campo obrigatório"
            }
        }