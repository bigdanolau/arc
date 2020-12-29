from django.db import models
import datetime
# Create your models here.
class SeguimientoModel(models.Model):

    titulo = models.TextField(max_length = 20, default="")
    contenido = models.TextField(max_length = 40,default="")
    # contenido = models.TextField(max_length = 40,default="")
    id_asignado = models.ForeignKey("users.User", on_delete=models.CASCADE, default="",limit_choices_to={'tipo': 'E'})
    id_condominio = models.ForeignKey("users.User", on_delete=models.CASCADE, default="",limit_choices_to={'tipo': 'C'},related_name="condominio_id")
    fecha_vencimiento = models.DateField(default=datetime.date.today)
    fecha_creacion = models.DateField( auto_now_add=True)
    id_apartamento = models.IntegerField(default='')
    file = models.FileField(upload_to='uploads', max_length=1000,default='')
    prueba = models.ManyToManyField("condominio.Condominio", default="",db_table='id_apartamento')
    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "tareas"

    def __str__(self):
        return self.titulo
