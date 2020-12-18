import datetime
from django.shortcuts import render
from django.db.models import Sum
from tablib import Dataset
from django.views.generic import ListView
from .models import Condominio
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import DeudaMixin,EstadisticasMixin
from applications.pagos.mixins import PagosMixin
class CondominioListView(EstadisticasMixin,PagosMixin,DeudaMixin,LoginRequiredMixin,ListView):
    login_url = reverse_lazy("Users:login")
    context_object_name = "deudasMes"
    model = Condominio
    template_name = "user/home.html"
    
    def get_queryset(self):
        usuario = self.request.user.id
        if(not self.request.GET.get('fecha')):
           
            return Condominio.objects.listar_mes(usuario)
        else:
            return Condominio.objects.buscar_mes(self.request.GET.get('fecha'),self.request.GET.get('fecha_uno'),usuario)
    

class ImportarExcel(ListView):
    model = Condominio
    template_name = "user/importar.html"
    def post(self, request):
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data =  Dataset().load(new_persons.read().decode("utf-8"), format='csv', headers=False)
        for data in imported_data:
            if (data[2] != "PROPIETARIO" and data[2] != ""):
               
                Condominio.objects.create(
                fecha=datetime.datetime.strptime(data[0],"%Y-%m-%d"),
                propietario=data[2],
                torre=data[3],
                apartamento = data[4],
                total_mes = data[14].replace(' ', '').replace('$','').replace(',',''),
                id_usuario = request.user.id,
                id_apartamento = str(request.user.id)+data[3]+''+data[4],
                total_mes_log = data[14].replace(' ', '').replace('$','').replace(',',''),
                )
            
            #print(data[15].replace(' ', '').replace('$',''))
            """print(data[0], data[1], data[2], data[3], data[4])"""
        return render(request, 'user/importar.html')

# Create your views here.
