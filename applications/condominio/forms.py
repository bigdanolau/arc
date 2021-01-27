from django import forms
from applications.pagos.models import Pago

class AddAbono(forms.ModelForm):
    monto = forms.CharField(
        required=True,
        label="Monto",
        widget= forms.TextInput(
            attrs = {
                'placeholder': 'Monto',
                'class': 'form-control',
                
            }
        )
        )
    id_apartamento = forms.CharField(
        required=True,
        label="",
        widget= forms.TextInput(
            attrs = {
                'placeholder': '',
                'class': 'form-control',
                'type': 'hidden'
            }
        )
        )
    nombre_propietario = forms.CharField(
        required=True,
        label="",
        widget= forms.TextInput(
            attrs = {
                'placeholder': '',
                'class': 'form-control',
                'type': 'hidden'
            }
        )
        )
    id_usuario = forms.CharField(
        required=True,
        label="",
        widget= forms.TextInput(
            attrs = {
                'placeholder': '',
                'class': 'form-control',
                'type': 'hidden'
            }
        )
        )
   
    fecha = forms.DateField(
        required=True,
        label="Fecha",
        
     
        widget= forms.DateInput(
            attrs = {
                
                'placeholder': 'Fecha del abono',
                'class': 'form-control',
                'type': 'date'
            }
        ) 
        )
        
   
    class Meta:
        model = Pago
        fields = ["monto","fecha","id_usuario","id_apartamento","nombre_propietario","deuda"]


