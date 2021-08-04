from django.urls import path
from .views import CotizacionView

urlpatterns = [
    path('cotizacion/', CotizacionView.as_view(), name='cotizacion'),
    path("cotizacion/<int:monto>", CotizacionView.as_view(), name="processs")
]