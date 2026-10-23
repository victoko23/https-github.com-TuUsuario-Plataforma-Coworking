from django.urls import path, include
from rest_framework import routers
from . import views

# Creamos el enrutador
enrutador = routers.DefaultRouter()

# Registramos las rutas para el CRUD
enrutador.register(r'espacios', views.EspacioViewSet)
enrutador.register(r'clientes', views.ClienteViewSet) # <--- ESTA LÍNEA ES CLAVE
enrutador.register(r'reservas', views.ReservaViewSet)

urlpatterns = [
    path('api/', include(enrutador.urls)),
]