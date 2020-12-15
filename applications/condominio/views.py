import datetime
from django.shortcuts import render
from django.db.models import Sum
from tablib import Dataset
from django.views.generic import ListView
from .models import Condominio

class CondominioListView(ListView):
    context_object_name = "deudasMes"
    model = Condominio
    template_name = "user/home.html"
    def get_queryset(self):
        if(not self.request.GET.get('fecha')):
           
            return Condominio.objects.listar_mes()
        else:
            return Condominio.objects.buscar_mes(self.request.GET.get('fecha'),self.request.GET.get('fecha_uno'))
    
    def get_context_data(self, **kwargs):
        context = super(CondominioListView, self).get_context_data(**kwargs)
        if(not self.request.GET.get('fecha')):
            context.update({
                'totalMes': Condominio.objects.listar_mes().aggregate(Sum('total_mes')).get('total_mes__sum',0.00),
                'totalGlobal': Condominio.objects.aggregate(Sum('total_mes')).get('total_mes__sum',0.00),
            })
        else:
            context.update({
                'totalMes': Condominio.objects.buscar_mes(self.request.GET.get('fecha'),self.request.GET.get('fecha_uno')).aggregate(Sum('total_mes')).get('total_mes__sum',0.00),
                'totalGlobal': Condominio.objects.aggregate(Sum('total_mes')).get('total_mes__sum',0.00),
                'fecha': self.request.GET.get('fecha'),
                'fecha_uno' : self.request.GET.get('fecha_uno'),
                
                #'var2': self.kwargs.get('var2', None),
            })
        return context


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
                total_mes = data[14].replace(' ', '').replace('$','').replace(',','')
                )
            
            #print(data[15].replace(' ', '').replace('$',''))
            """print(data[0], data[1], data[2], data[3], data[4])"""
        return render(request, 'user/importar.html')

# Create your views here.
