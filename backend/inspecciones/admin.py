from django.contrib import admin
from .models import Inspeccion

@admin.register(Inspeccion)
class InspeccionAdmin(admin.ModelAdmin):
    list_display = ('direccion', 'fecha', 'estado', 'inspector', 'creado_en')
    list_filter = ('estado', 'fecha')
    search_fields = ('direccion', 'inspector')
