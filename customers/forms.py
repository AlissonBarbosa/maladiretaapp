from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        labels = {
            'name': 'Nome',
            'birth': 'Nascimento',
            'nickname': 'Pseudonimo',
            'reference': 'Referência',
            'city': 'Cidade',
            'street': 'Rua',
            'number': 'Número',
            'complement': 'Complemento',
            'cep': 'CEP',
            'state': 'Estado',
            'neighborhood': 'Bairro',
            'rg': 'RG',
            'cpf': 'CPF',
            'phone_number': 'Telefone',
            'cellphone': 'Celular',
            'phone_home': 'Residencial',
            'leadership': 'Liderança',
            'subscription': 'Inscrição',
            'zone': 'Zona',
            'section': 'Seção',
            'profession': 'Profissão'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'birth': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'nickname': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'reference': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'city': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'street': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'number': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'complement': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'cep': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off', 'data-mask':"00.000-000"}),
            'state': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'neighborhood': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'rg': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'cpf': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off', 'placeholder': 'xxx.xxx.xxx-xx', 'data-mask':"000.000.000-00"}),
            'phone_number': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off', 'placeholder': '(xx)xxxx-xxxx', 'data-mask':"(00)0000-0000"}),
            'phone_home': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off', 'placeholder': '(xx)xxxx-xxxx', 'data-mask':"(00)0000-0000"}),
            'cellphone': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off', 'placeholder': '(xx)xxxxx-xxxx', 'data-mask':"(00)00000-0000"}),
            'leadership': forms.Select(attrs={'class':"form-control cc-name valid"}),
            'subscription': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'zone': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'section': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'email': forms.EmailInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'profession': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'})
        }
        error_messages = {
            'name': {
                'required': "Nome é um campo obrigatório"
            }
        }