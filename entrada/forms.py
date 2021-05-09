from django import forms
from .models import NotasEntradas


class FormNotasEntradas(forms.ModelForm):

    class Meta:
        model = NotasEntradas
        fields = [
            'produto',
            'quantidade',
            'preco',
        ]
