from django import forms
from .models import User



class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label="Usuario",
        widget= forms.TextInput(
            attrs = {
                'placeholder': 'Usuario',
                'class': 'form-control'
            }
        )
        )
    password = forms.CharField(
        required=True,
        label="Contraseña",
        widget= forms.PasswordInput(
            attrs = {
                'placeholder': 'Contraseña',
                'class': 'form-control'
            }
        )
        )


