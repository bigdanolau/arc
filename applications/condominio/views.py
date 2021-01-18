import datetime
from django.shortcuts import render
from django.db.models import Sum
from tablib import Dataset
from django.views.generic import ListView,FormView
from .models import Condominio
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import DeudaMixin,EstadisticasMixin
from applications.pagos.mixins import PagosMixin
from .forms import AddAbono
from applications.pagos.models import Pago
class CondominioListView(EstadisticasMixin,PagosMixin,DeudaMixin,LoginRequiredMixin,FormView):
    login_url = reverse_lazy("Users:login")
    context_object_name = "deudasMes"
    model = Condominio
    template_name = "user/home.html"
    form_class = AddAbono
    success_url = "/home"
    def form_valid(self,form):
      
       
        date1 = datetime.datetime.strptime(str(form.cleaned_data['fecha']),'%Y-%m-%d').date()
      
        abono = Pago(
            monto = int(form.cleaned_data['monto'].replace('.','').replace(',','')),
            fecha = date1,
            deuda = form.cleaned_data['deuda'],
            id_usuario = form.cleaned_data['id_usuario'],
            id_apartamento = form.cleaned_data['id_apartamento'],
            nombre_propietario = form.cleaned_data['nombre_propietario']
        )
        abono.save()
        return super(CondominioListView,self).form_valid(form)

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
                numero_meses = data[5],
                total_mes = data[14].replace(' ', '').replace('$','').replace(',',''),
                id_usuario = request.user.id,
                id_apartamento = str(request.user.id)+data[3]+''+data[4],
                total_mes_log = data[14].replace(' ', '').replace('$','').replace(',',''),
                )
            
            #print(data[15].replace(' ', '').replace('$',''))
            """print(data[0], data[1], data[2], data[3], data[4])"""
        return render(request, 'user/importar.html')

# Create your views here.
