from .models import Condominio
from django.db.models import Sum
from applications.pagos.models import Pago
class DeudaMixin(object):
    
    def get_context_data(self, **kwargs):
        usuario = self.request.user.id
        context = super(DeudaMixin, self).get_context_data(**kwargs)
        if(not self.request.GET.get('fecha')):
            context.update({
                'totalMes': Condominio.objects.listar_mes(usuario).aggregate(Sum('total_mes_log')).get('total_mes_log__sum',0.00),
                'totalGlobal': Condominio.objects.aggregate(Sum('total_mes')).get('total_mes__sum',0.00),
            })
        else:
            context.update({
                'totalMes': Condominio.objects.buscar_mes(self.request.GET.get('fecha'),self.request.GET.get('fecha_uno'),usuario).aggregate(Sum('total_mes_log')).get('total_mes_log__sum',0.00),
                'totalGlobal': Condominio.objects.aggregate(Sum('total_mes')).get('total_mes__sum',0.00),
                'fecha': self.request.GET.get('fecha'),
                'fecha_uno' : self.request.GET.get('fecha_uno'),
                
                #'var2': self.kwargs.get('var2', None),
            })
        return context
  
class EstadisticasMixin(object):
    
    
    def get_context_data(self, **kwargs):
        usuario = self.request.user.id
        context = super(EstadisticasMixin, self).get_context_data(**kwargs)
        total_deuda_mes = None
        if( self.request.GET.get('fecha')):
            total_deuda_mes = Condominio.objects.buscar_mes(self.request.GET.get('fecha'),self.request.GET.get('fecha_uno'),usuario).aggregate(Sum('total_mes')).get('total_mes__sum',0.00)
        
        total_pagos_mes =  Pago.objects.listar_mes(usuario).aggregate(Sum('monto')).get('monto__sum',0.00)
        if(not total_deuda_mes is None and not total_pagos_mes is None) :
            context['porcentaje_mes'] =  ((total_deuda_mes - total_pagos_mes)/ total_deuda_mes ) * 100
            context['porcentaje_mes'] =  ((total_deuda_mes - total_pagos_mes)/ total_deuda_mes ) * 100
            
        else:
            context['porcentaje_mes'] =  0
            context['porcentaje_mes'] =  0
            
        
        return context
    
