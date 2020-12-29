from django.shortcuts import render
from django.views.generic import FormView
# Create your views here.

from .models import SeguimientoModel


class TareasListView(FormView):
    model = SeguimientoModel
    template_name = "tareas/home.html"
