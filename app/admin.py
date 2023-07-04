# -*- coding: UTF-8 -*-

from django.contrib import admin
from .models import Partido, Candidato, Eleccion, Country, Region, SubRegion, City, CargoElecto


admin.site.site_title = "Elecciones"
admin.site.site_header = "Elecciones"
admin.site.index_title = "Elecciones"


@admin.register(CargoElecto)
class CargoElectoAdmin(admin.ModelAdmin):
    pass


@admin.register(Partido)
class PartidoAdmin(admin.ModelAdmin):
    list_display = ["partido", "thumb_partido"]


@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "partido", "thumb_partido"]


@admin.register(Eleccion)
class EleccionAdmin(admin.ModelAdmin):
    list_display = ["__str__", "fecha_comicios"]


admin.site.unregister(Country)
admin.site.unregister(Region)
admin.site.unregister(SubRegion)
admin.site.unregister(City)
