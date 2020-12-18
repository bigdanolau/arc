from django.db import models

# Create your models here.
class TareaModel(models.Model):

    titulo = models.TextField(max_length = 20)

    class Meta:
        verbose_name = "TareaModel"
        verbose_name_plural = "TareaModels"

    def __str__(self):
        return self.titulo
