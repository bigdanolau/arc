from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.

from .models import TareaModel


class TareasListView(ListView):
    model = TareaModel
    template_name = "tareas/home.html"
