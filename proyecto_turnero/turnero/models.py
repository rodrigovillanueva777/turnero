from django.db import models

# Create your models here.

class Cliente(models.Model):
    PRIORIDAD_CHOICES = (
        (1, 'Baja'),
        (2, 'Media'),
        (3, 'Alta'),
    )
    BOXES_CHOICES = (
        (1, 'Box 1'),
        (2, 'Box 2'),
        (3, 'Box 3'),
    )

    nombre = models.CharField(max_length=100)
    cedula_ruc = models.CharField(max_length=20, unique=True)
    turno = models.AutoField(primary_key=True)
    prioridad = models.IntegerField(choices=PRIORIDAD_CHOICES)
    servicios = models.IntegerField(choices=BOXES_CHOICES)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    atendido = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre