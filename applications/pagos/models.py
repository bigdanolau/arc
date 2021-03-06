from django.db import models
from applications.condominio.models import Condominio
from datetime import datetime
# Create your models here.
from .managers import PagoaManager
class Pago(models.Model):
    
    monto = models.IntegerField(null=False)
    fecha = models.DateField(null= False,default=datetime.now)
    deuda = models.ForeignKey(Condominio, on_delete=models.CASCADE,null=False)
    id_usuario = models.IntegerField(null=False)
    id_apartamento = models.IntegerField(null=False)
    nombre_propietario = models.TextField()
    numero_factura = models.TextField(default="0")
    objects = PagoaManager()

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"

    def __str__(self):
        return self.nombre_propietario

