from django.contrib import admin
from django.urls import path, include
from coworking import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.bienvenida, name='bienvenida'), # Carga tu HTML
    path('coworking/', include('coworking.urls')), # <--- ESTA LÍNEA ES CLAVE
]