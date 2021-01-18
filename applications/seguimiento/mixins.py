from .models import SeguimientoModel
from ..condominio.models import Condominio
class TareasMixin(object):
    
    
    def get_context_data(self, **kwargs):
        context = super(TareasMixin, self).get_context_data(**kwargs)
        context.update({
                'apartamento': Condominio.objects.listar_mes(1),
                
        })
        return context
