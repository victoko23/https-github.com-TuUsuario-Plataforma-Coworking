from django.shortcuts import render
from rest_framework import viewsets
from .models import Espacio, Cliente, Reserva
from .serializers import EspacioSerializer, ClienteSerializer, ReservaSerializer

def bienvenida(request):
    return render(request, 'Bienvenido.html')

class EspacioViewSet(viewsets.ModelViewSet):
    queryset = Espacio.objects.all()
    serializer_class = EspacioSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer