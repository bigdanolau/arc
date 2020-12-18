from .models import Pago
from django.db.models import Sum
class PagosMixin(object):
      
      def get_context_data(self, **kwargs):
          usuario = self.request.user.id
          fecha = self.request.GET.get('fecha')
          fecha_uno = self.request.GET.get('fecha_uno')
          context = super(PagosMixin, self).get_context_data(**kwargs)
          if(not self.request.GET.get('fecha')):
                
                context['pagos'] = Pago.objects.listar_mes(usuario)
                context['pagosTotalMes'] = Pago.objects.listar_mes(usuario).aggregate(Sum('monto')).get('monto__sum',0.00)
          else:
                context['pagos'] = Pago.objects.buscar_mes(fecha,fecha_uno,usuario)
                context['pagosTotalMes'] = Pago.objects.listar_mes(usuario).aggregate(Sum('monto')).get('monto__sum',0.00)
                context['PagostotalGlobal'] =  Pago.objects.aggregate(Sum('monto')).get('monto__sum',0.00),
                
          return context
 