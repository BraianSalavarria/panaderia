from django import forms
from Apps.ventas.models import Categoria, Venta, ItemVenta


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'nombre de categoria'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control  form-control-sm'


class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['nro_comprobante', 'comprobante_tipo', 'venta_tipo', 'pago_tipo', 'observaciones']
        widgets = {
            'nro_comprobante': forms.TextInput(attrs={'class':'form-control form-control-sm text-black'}),
            'comprobante_tipo': forms.Select(attrs={'class':'form-select text-black'}),
            'venta_tipo': forms.Select(attrs={'class':'form-select text-black'}),
            'pago_tipo': forms.Select(attrs={'class':'form-select text-black'}),
            'observaciones': forms.Textarea(attrs={'rows': '6', 'cols': '8','class':'form-control form-control-sm text-black'}),
        }


class ItemVentaForm(forms.ModelForm):
    class Meta:
        model = ItemVenta
        fields = ['producto','cantidad']
        widgets = {
                    'producto': forms.Select(attrs={'class':'form-select text-black'}),
                    'cantidad': forms.NumberInput(attrs={'min':'1','value':'1','class':'form-control  form-control-sm'})
                   }

#creamos los formset para la venta

ItemsVentaFormSet = forms.inlineformset_factory(
    Venta,
    ItemVenta,
    form=ItemVentaForm,
    extra=1,
    can_delete=False,
)
