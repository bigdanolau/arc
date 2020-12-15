import datetime
from django.db import models
class DeudasManager (models.Manager):
    def buscar_mes(self,fecha,fecha_dos):
        date1 = datetime.datetime.strptime(fecha,'%Y-%m-%d').date()
        date2 = datetime.datetime.strptime(fecha_dos,'%Y-%m-%d').date()
        resultado = self.filter(
            fecha__range=(date1,date2)

        )
        return resultado

    def listar_mes(self):
        today = datetime.datetime.today()
        date1 = datetime.datetime(today.year, today.month, 1)
        date2 = datetime.datetime(today.year, today.month, today.day)
        
        resultado = self.filter(
            fecha__range=(date1,date1)
        )
        return resultado