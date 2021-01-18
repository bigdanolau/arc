from django.db import models
import datetime
from .managers import SeguimientoManager
# Create your models here.
class SeguimientoModel(models.Model):

    titulo = models.CharField(max_length = 20, default="")
    contenido = models.TextField(default="")
    # contenido = models.TextField(max_length = 40,default="")
    id_asignado = models.ForeignKey("users.User", on_delete=models.CASCADE, default="",limit_choices_to={'tipo': 'E'})
    id_condominio = models.ForeignKey("users.User", on_delete=models.CASCADE, default="",limit_choices_to={'tipo': 'C'},related_name="condominio_id")
    fecha_vencimiento = models.DateField(default=datetime.date.today)
    fecha_creacion = models.DateField( auto_now_add=True)
    id_apartamento = models.CharField(default='',max_length = 20)
    fecha_actualizacion = models.DateField(auto_now=True)
    file = models.FileField(upload_to='uploads', max_length=1000,default='',blank=True)
    # prueba = models.ManyToManyField("condominio.Condominio", default="",db_table='id_apartamento')
    estado = models.BooleanField(default=False)
    objects = SeguimientoManager()
    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "tareas"

    def __str__(self):
        return self.titulo
