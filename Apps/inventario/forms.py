from django import forms

from Apps.inventario.models import Proveedor


class ProveedorForm(forms.ModelForm):
    class Meta:
        model= Proveedor
        fields =['nombre','apellido','empresa']

        widgets = {
            'nombre' : forms.TextInput(attrs={'placeholder':'nombre'}),
            'apellido' : forms.TextInput(attrs={'placeholder':'apellido'}),
            'empresa' : forms.TextInput(attrs={'placeholder':'nombre de la empresa o fabrica'}),
        }

    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = "form-control form-control-sm"