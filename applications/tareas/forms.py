from django import forms
from .models import TareaModel
class TareasFormulario(forms.Form):
    """FORMNAME definition."""

    # TODO: Define form fields here
    
    class meta:
        model= TareaModel
        fields: ['']