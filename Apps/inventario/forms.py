


from django import forms

from Apps.inventario.models import Proveedor, Pedido, ItemPedido, PedidoRecibido, ItemPedidoRecicido



class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'apellido', 'empresa']

        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'nombre'}),
            'apellido': forms.TextInput(attrs={'placeholder': 'apellido'}),
            'empresa': forms.TextInput(attrs={'placeholder': 'nombre de la empresa o fabrica'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = "form-control form-control-sm"



class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nro_pedido', 'observaciones', ]
        widgets = {
                'nro_pedido': forms.TextInput(attrs={'class': 'form-control form-control-sm text-black'}),
                'observaciones': forms.Textarea(attrs={'rows': '6', 'cols': '8', 'class': 'form-control form-control-sm text-black'}),

        }

class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields=['insumo','cantidad']
        widgets={
            'insumo': forms.Select(attrs={'class':'form-select form-select-sm text-black'}),
            'cantidad': forms.NumberInput(attrs={
                'min':'1',
                'value':'1',
                'class':'form-control form-control-sm',
                'style': 'width: 100px'})
        }


ItemsPedidosFormSet = forms.inlineformset_factory(
    Pedido,
    ItemPedido,
    form=ItemPedidoForm,
    extra=1,
    can_delete=False,
    )



class ItemPedidoRecibidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedidoRecicido
        fields = ['insumo','cantidad','precio_unit','total']
        widgets = {
            'insumo' : forms.Select(attrs={'class':'form-select form-select-sm text-black','required':'true'}),
            'cantidad': forms.NumberInput(attrs={
                'min': '1',
                'class': 'form-control form-control-sm',
                'style': 'width: 100px','required':'true'}),
            'precio_unit': forms.NumberInput(attrs={
                'min': '1',
                'class': 'form-control form-control-sm',
                'style': 'width: 100px','required':'true'}),
            'total': forms.NumberInput(attrs={
                'min': '1',
                'class': 'form-control form-control-sm',
                'style': 'width: 100px','required':'true'})
        }



ItemsPedidosRecibidoFormSet = forms.inlineformset_factory(
    PedidoRecibido,
    ItemPedidoRecicido,
    form= ItemPedidoRecibidoForm,
    extra=1,
    can_delete=False,
)






