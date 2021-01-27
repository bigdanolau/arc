from django.shortcuts import render
from django.views.generic import CreateView
from .models import ComentarioModel
# Create your views here.



class ComentarioCreateView(CreateView):
    model = ComentarioModel
    template_name = "tareas/addComentario.html"
    fields = ('__all__')