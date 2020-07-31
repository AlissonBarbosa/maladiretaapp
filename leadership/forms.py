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
            'neighborhood': 'Bairro'
        }