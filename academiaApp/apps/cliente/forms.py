from django import forms
from .models import Cliente


class FormCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'  # Inclui todos os campos do model

        widgets = {
            "nome": forms.TextInput(attrs={"class": "input-large", "placeholder": "Digite seu nome completo"}),
            "sobrenome": forms.TextInput(attrs={"class": "input-large", "placeholder": "Digite seu sobrenome"}),
            "email": forms.EmailInput(attrs={"class": "input-email", "placeholder": "exemplo@dominio.com"}),
            "endereco": forms.Textarea(attrs={"class": "textarea-endereco", "rows": 3}),
            "genero": forms.RadioSelect(attrs={"class": "radio-genero"}),
            "item_cliente": forms.CheckboxSelectMultiple(attrs={"class": "checkbox-itens"}),
        }