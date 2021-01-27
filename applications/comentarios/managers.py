from django.db import models
class ComentarioManager(models.Manager):
    
    def get_comentarios(self,id_tarea):
        resultado = self.filter(
            id_tarea = id_tarea
        )
        return resultado
    def get_queryset(self):
        return super().get_queryset().filter()
