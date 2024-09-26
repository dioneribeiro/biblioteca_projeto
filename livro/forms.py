from django import forms
from .models import Livros

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livros
        fields = ['nome', 'autor', 'co_autor', 'img_capa', 'sinopse', 'categoria', 'usuario']
