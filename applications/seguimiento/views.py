from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,TemplateView
# Create your views here.
from .models import SeguimientoModel
from ..condominio.models import Condominio
from ..pagos.models import Pago
from .mixins import TareasMixin
class TareasListView(ListView,):
    model = SeguimientoModel
    template_name = "tareas/home.html"
    
    def post(self,request):
        SeguimientoModel.objects.update(request.POST['id'],request.POST['estado'])
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tareas'] = SeguimientoModel.objects.listar_tareas(self.request.user)
        return context
class listadoTarea(ListView):
    model = SeguimientoModel
    template_name = "tareas/listado.html"
    
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tareas'] = SeguimientoModel.objects.listar_tareas_user(self.kwargs['pk'],self.request.user)
        context['deuda'] = Condominio.objects.buscar_usuario(self.kwargs['pk'])
        context['pagos'] = Pago.objects.pago_apartamento(self.kwargs['pk'])
        return context

class detalleTarea(TemplateView,TareasMixin): 
    
    template_name = "tareas/detalle.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.kwargs['pk'])
        context['tarea'] = SeguimientoModel.objects.traer(self.kwargs['pk'])
        context['deuda'] = Condominio.objects.buscar_usuario(self.kwargs['deuda'])
        
        return context
    
class CrearTarea(CreateView): 
    # specify the model to use 
    model = SeguimientoModel
    success_url = '/'
    template_name = "tareas/crear.html"
    fields = ('__all__')
