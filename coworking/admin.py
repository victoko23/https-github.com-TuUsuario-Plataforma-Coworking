from django.contrib import admin
from .models import Espacio, Cliente, Reserva

# Registramos los modelos para que aparezcan en el panel
@admin.register(Espacio)
class EspacioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'capacidad', 'precio_por_hora', 'disponible')
    search_fields = ('nombre',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rut', 'email', 'telefono')
    search_fields = ('nombre', 'rut')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'espacio', 'fecha_reserva', 'estado')
    list_filter = ('estado', 'fecha_reserva')