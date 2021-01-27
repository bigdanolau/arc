from django.db import models
from .managers import ComentarioManager
# Create your models here.
class ComentarioModel(models.Model):

    id_tarea = models.ForeignKey("seguimiento.SeguimientoModel", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    archivo = models.FileField(blank=True)
    fecha_ingreso = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey("users.User", on_delete=models.CASCADE,default=1)
    objects = ComentarioManager()
    class Meta:
        verbose_name = "ComentarioModel"
        verbose_name_plural = "ComentarioModels"

    def __str__(self):
        return self.titulo