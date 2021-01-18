from django.db import models
class SeguimientoManager (models.Manager):
    def listar_tareas(self,usuario):
        resultado = self.filter(
            id_asignado = usuario,
        ).order_by('fecha_vencimiento')
        return resultado
 
    def listar_tareas_user(self,condominio,usuario):
        resultado = self.filter(
            id_apartamento = condominio,
        ).order_by('fecha_vencimiento')
        return resultado
 
    def update(self,id,estado):
        self.filter(
                id = id
            ).update(estado = estado)
    def traer(self,id):
        resultado  = self.filter(
                id = id
        )
        return resultado[0]