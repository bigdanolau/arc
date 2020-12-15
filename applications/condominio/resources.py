from import_export import resources
from .models import Condominio

class CondominioResource(resources.ModelResource):
    class Meta:
        model = Condominio