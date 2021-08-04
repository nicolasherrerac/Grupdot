from django.views import View
from django.utils.decorators import method_decorator
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import Impresion, Vf

class CotizacionView(View):
    """View de la cotizacion del cliente para el prestamo"""
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, monto=0):
        """Funcion que consulta la api de prestamos"""
        if monto >= 0 and monto <= 3000000:
            valor = Vf(0.012, monto)
            impresion = Impresion('María', valor, '1.2%')
        elif monto > 3000000 and monto <= 5000000:
            valor = Vf(0.015, monto)
            impresion = Impresion('Juan', valor, '1.5%')
        elif monto > 5000000 and monto <= 7500000:
            valor = Vf(0.02, monto)
            impresion = Impresion('Andrés', valor, '2.0%')
        elif monto > 7500000:
            datos = {'messenge': "No hay socio disponible"}
            return JsonResponse(datos)
        return impresion
