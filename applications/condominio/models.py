from django.db import models
from .managers import DeudasManager
# Create your models here.

class Condominio(models.Model):
    objects = DeudasManager()
    fecha = models.DateField(auto_now=False)
    fecha_registro = models.DateField(auto_now_add=True)
    propietario = models.TextField();
    torre = models.TextField(max_length = 4)
    apartamento = models.TextField(max_length= 4)
    id_apartamento = models.TextField(max_length= 10,default="")
    numero_meses = models.TextField(default="1")
    id_usuario = models.TextField(max_length= 10,default="")
    total_mes = models.TextField()
    total_mes_log = models.TextField(default="")
    def __str__(self):
        return str(self.id_apartamento) 

    class Meta:
        verbose_name = 'Condominio'
        verbose_name_plural = 'Condominios'