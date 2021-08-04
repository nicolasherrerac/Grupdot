from django.views import View
from django.utils.decorators import method_decorator
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import Vf
class CotizacionView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, monto=0):
        if monto >= 0 and monto <= 3000000:
            valor = Vf(0.012, monto)
            return JsonResponse({'Valor Futuro': valor, 'Cuotas Mensuales': int(valor/36), 'Socio Prestamista': 'María'})
        elif monto > 3000000 and monto <= 5000000:
            valor = Vf(0.015, monto)
            return JsonResponse({'Valor Futuro': int(valor), 'Cuotas Mensuales': int(valor/36), 'Socio Prestamista': 'Juan'})
        elif monto > 5000000 and monto <= 7500000:
            valor = Vf(0.02, monto)
            return JsonResponse({'Valor Futuro': valor, 'Cuotas Mensuales': int(valor/36), 'Socio Prestamista': 'Andrés'})
        elif monto > 7500000:
            datos = {'messenge': "No hay socio disponible"}
            return JsonResponse(datos)