from django.shortcuts import render
from django.views.generic import FormView
# Create your views here.

from .models import TareaModel


class TareasListView(FormView):
    model = TareaModel
    template_name = "tareas/home.html"
