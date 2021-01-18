from django import forms
from .models import User
from django.contrib.auth import authenticate


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
    
    
    def clean(self):
        cleaned_data = super(LoginForm,self).clean()
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]
            
        if not authenticate(username=username,password=password):
            raise forms.ValidationError('Datos erroneos')
        return self.cleaned_data
        

class RegisterForm(forms.Form):
    CHOICES = [
        ('C',"Condominio"),
        ('A',"administrador"),
        ('E',"Empleado")
    ]
    username = forms.CharField(
        required=True,
        label="",
        widget= forms.TextInput(
            attrs = {
                'placeholder': 'Usuario',
                'class': 'form-control'
            }
        )
        )
    password = forms.CharField(
        required=True,
        label="",
        widget= forms.PasswordInput(
            attrs = {
                'placeholder': 'Contraseña',
                'class': 'form-control'
            }
        )
        )
    email = forms.CharField(
        required=True,
        label="",
        widget= forms.TextInput(
            attrs = {
                'type': 'email',
                'placeholder': 'Email',
                'class': 'form-control'
            }
        )
        )
    nombre = forms.CharField(
        required=True,
        label="",
        widget= forms.TextInput(
            attrs = {
                'placeholder': 'Nombre',
                'class': 'form-control'
            }
        )
        )
    empresa = forms.CharField(
        required=True,
        label="",
        widget= forms.TextInput(
            attrs = {
                'placeholder': 'Empresa',
                'class': 'form-control'
            }
        )
        )
    tipo = forms.ChoiceField(
        label="",
        choices=CHOICES,
        required = True
    )
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'nombre',
            'empresa',
            'tipo',
            'password'
        ]
    
        


