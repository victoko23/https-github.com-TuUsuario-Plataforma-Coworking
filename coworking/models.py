from django.db import models

class Espacio(models.Model):
    TIPO_CHOICES = [
        ('oficina', 'Oficina Privada'),
        ('sala', 'Sala de Reuniones'),
        ('escritorio', 'Escritorio Flexible'),
    ]
    nombre = models.CharField("Nombre", max_length=100, null=False)
    tipo = models.CharField("Tipo", max_length=20, choices=TIPO_CHOICES, default='escritorio')
    capacidad = models.PositiveIntegerField("Capacidad", default=1)
    precio_por_hora = models.DecimalField("Precio por Hora", max_digits=8, decimal_places=2)
    disponible = models.BooleanField("Disponible", default=True)
    habilitado = models.BooleanField("Habilitado", default=True)
    created_at = models.DateTimeField("Fecha Creación", auto_now_add=True)
    updated_at = models.DateTimeField("Fecha Actualización", auto_now=True)

    class Meta:
        db_table_comment = "Data de espacios de coworking disponibles para reserva."

    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_display()})"

class Cliente(models.Model):
    nombre = models.CharField("Nombre Completo", max_length=100, null=False)
    rut = models.CharField("RUT", max_length=12, unique=True)
    email = models.EmailField("Correo", null=True, blank=True) # <-- blank=True agregado
    telefono = models.CharField("Teléfono", max_length=15, null=True, blank=True) # <-- blank=True agregado
    created_at = models.DateTimeField("Fecha Creación", auto_now_add=True)

    class Meta:
        db_table_comment = "Registro de clientes que reservan espacios."

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('pagada', 'Pagada'),
        ('cancelada', 'Cancelada'),
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    espacio = models.ForeignKey(Espacio, on_delete=models.CASCADE, verbose_name="Espacio")
    fecha_reserva = models.DateTimeField("Fecha y Hora de Reserva")
    estado = models.CharField("Estado", max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    created_at = models.DateTimeField("Fecha Creación", auto_now_add=True)

    class Meta:
        db_table_comment = "Registro de reservas de espacios por parte de los clientes."

    def __str__(self):
        return f"Reserva de {self.cliente.nombre} en {self.espacio.nombre}"