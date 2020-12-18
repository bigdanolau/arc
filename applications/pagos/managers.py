import datetime
from django.db import models
class PagoaManager(models.Manager):
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
        date1 = datetime.datetime(today.year, today.month, 1)
        date2 = datetime.datetime(today.year, today.month, today.day)
        
        resultado = self.filter(
            id_usuario = usuario,
            fecha__range=(date1,date2),
        )
        return resultado
    