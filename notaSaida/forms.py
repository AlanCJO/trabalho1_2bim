from django import forms
from .models import NotaSaida


class FormNotaSaida(forms.ModelForm):

    class Meta:
        model = NotaSaida
        fields = [
            'produto',
            'numero_nota',
            'quantidade',
            'valor'
        ]