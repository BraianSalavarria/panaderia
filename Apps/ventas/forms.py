from dataclasses import field
from django import forms
from Apps.ventas.models import Categoria


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

        widgets = {
            'nombre' : forms.TextInput(attrs={'placeholder':'nombre de categoria'})
        }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control  form-control-sm'
