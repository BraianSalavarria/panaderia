from dataclasses import fields

from django import forms
from django.conf.locale.az.formats import DATETIME_INPUT_FORMATS

from Apps.empleados.models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['cuil','nombre','apellido','telefono_celular','telefono_fijo','calle','nro_calle','localidad','dpto','fecha_nacimiento','fecha_ingreso']
        telefono_fijo = forms.CharField(required=False)
        widgets = {
            'cuil' : forms.TextInput(attrs={'placeholder':'ingrese cuil'}),
            'nombre' : forms.TextInput(attrs={'placeholder':'nombre de empleado',}),
            'apellido ' : forms.TextInput(attrs={'placeholder':'apellido de empleado'}),
            'telefono_celular' : forms.TextInput(attrs={'placeholder':'telefono celular'}),
            'telefono_fijo' : forms.TextInput(attrs={'placeholder': 'telefono fijo'}),
            'calle' : forms.TextInput(attrs={'placeholder':'nombre de calle'}),
            'nro_calle' : forms.NumberInput(attrs={'placeholer':'numero de calle'}),
            'localidad' : forms.TextInput(attrs={'placeholder':'nombre de la localidad'}),
            'dpto': forms.TextInput(attrs={'placeholder':'departamento'}),
            'fecha_nacimiento': forms.DateInput(format="%m/%d/%Y",attrs={'type':'date'}),
            'fecha_ingreso': forms.DateInput(format="%m/%d/%Y",attrs={'type':'date'}),
        }
    

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = "form-control form-control-sm"
