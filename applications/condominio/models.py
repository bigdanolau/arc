from django.db import models
from .managers import DeudasManager
# Create your models here.

class Condominio(models.Model):
    objects = DeudasManager()
    fecha = models.DateField(auto_now=False)
    fecha_registro = models.DateField( auto_now_add=True)
    propietario = models.TextField();
    torre = models.TextField(max_length = 4)
    apartamento = models.TextField(max_length= 4)
    total_mes = models.TextField()
    def __str__(self):
        return str(self.propietario) 

    class Meta:
        verbose_name = 'Condominio'
        verbose_name_plural = 'Condominios'