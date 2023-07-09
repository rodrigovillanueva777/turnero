from django.contrib import admin
from .models import Cliente

# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cedula_ruc','prioridad', 'fecha_hora', 'servicios','turno','atendido')
    list_editable = ('atendido',)
    search_fields = ('nombre', 'cedula_ruc','turno','prioridad', 'fecha_hora', 'servicios','atendido')
    pass
