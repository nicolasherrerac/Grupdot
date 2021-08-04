from django.http.response import JsonResponse

def Vf(interes, monto):
    """Funcion que me retorna el valor futuro"""
    valor = 1 + (36 * interes)
    valor *= monto
    return valor

def Impresion(socio, valor, tasa):
    """Funcion qu eme retorna un json con los parametros a imprimir"""
    return JsonResponse({'Socio que realiza el prestamo': socio,
                                'Cuotas Mensuales': int(valor/36),
                                'Credito total del prestamo': int(valor),
                                'Tasa de interes Mensual': tasa})