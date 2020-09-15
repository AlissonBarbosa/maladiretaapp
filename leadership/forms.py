from django import forms
from .models import Leadership

class LeadershipForm(forms.ModelForm):
    class Meta:
        model = Leadership
        fields = '__all__'
        labels = {
            'name': 'Nome',
            'phone_number': 'Telefone',
            'phone_home': 'Residencial',
            'cellphone': 'Celular',
            'city': 'Cidade',
            'street': 'Rua',
            'number': 'Número',
            'complement': 'Complemento',
            'cep': 'CEP',
            'state': 'Estado',
            'neighborhood': 'Bairro',
            'rg': 'RG',
            'cpf': 'CPF',
            'birth': 'Nascimento',
            'nickname': 'Pseudonimo',
            'note': 'Observação',
            'position': 'Cargo',
            'office': 'Cargo(Avulso)',
            'pendency': 'Pendência'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'phone_number': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off', 'placeholder': '(xx)xxxx-xxxx', 'data-mask':"(00)0000-0000"}),
            'phone_home': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off', 'placeholder': '(xx)xxxx-xxxx', 'data-mask':"(00)0000-0000"}),
            'cellphone': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off', 'placeholder': '(xx)xxxxx-xxxx', 'data-mask':"(00)00000-0000"}),
            'city': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'street': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'number': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'complement': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'cep': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off', 'placeholder': 'xx.xxx-xxx', 'data-mask':"00.000-000"}),
            'state': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'neighborhood': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'rg': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'cpf': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off', 'placeholder': 'xxx.xxx.xxx-xx', 'data-mask':"000.000.000-00"}),
            'birth': forms.DateInput(attrs={'class':"form-control cc-name valid", 'type':'text', 'autocomplete': 'off', 'placeholder': 'dd/mm/aaaa', 'data-mask':"00/00/0000"}),
            'nickname': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'note': forms.Textarea(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'email': forms.EmailInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'position': forms.Select(attrs={'class':"form-control cc-name valid"}),
            'office': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'}),
            'pendency': forms.TextInput(attrs={'class':"form-control cc-name valid", 'autocomplete': 'off'})
        }
        error_messages = {
            'name': {
                'required': "Nome é um campo obrigatório"
            }
        }