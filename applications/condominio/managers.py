import datetime
from django.db import models
class DeudasManager (models.Manager):
    def buscar_mes(self,fecha,fecha_dos,usuario):
        date1 = datetime.datetime.strptime(fecha,'%Y-%m-%d').date()
        date2 = datetime.datetime.strptime(fecha_dos,'%Y-%m-%d').date()
        resultado = self.filter(
            fecha__range=(date1,date2),
            id_usuario = usuario
        )
        return resultado

    def listar_mes(self,usuario):
        today = datetime.datetime.today()
      
        
        resultado = self.filter(
            fecha__month=today.month,
            id_usuario = usuario
        )
        return resultado
    
    
    def buscar_usuario(self,id_apartamento):
        resultado = self.filter(
            
            id_apartamento = id_apartamento
        ).order_by('id')[:1]
        return resultado[0]

   