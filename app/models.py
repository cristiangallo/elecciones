# -*- coding: UTF-8 -*-

from cities_light.abstract_models import (AbstractCity, AbstractRegion, AbstractSubRegion, AbstractCountry)
from cities_light.receivers import connect_default_signals
from sorl.thumbnail import ImageField as sorl_thumbnail_ImageField
from autoslug import AutoSlugField
from django.db import models


class Country(AbstractCountry):
    pass

    class Meta:
        verbose_name_plural = 'Países'
        verbose_name = 'País'


class Region(AbstractRegion):
    pass

    class Meta:
        verbose_name_plural = 'Provincias'
        verbose_name = 'Provincia'

    @property
    def descripcion(self):
        return u'%s' % self.name.split(" Province")[0]


class SubRegion(AbstractSubRegion):
    pass


class City(AbstractCity):
    pass

    class Meta:
        verbose_name_plural = u"Localidades"


connect_default_signals(Country)
connect_default_signals(Region)
connect_default_signals(SubRegion)
connect_default_signals(City)


class Partido(models.Model):
    partido = models.CharField(max_length=255)
    logo = sorl_thumbnail_ImageField(max_length=255, upload_to="imagenes/logos-partidos/")
    slug = AutoSlugField(populate_from='partido', unique=True, editable=False)

    def __str__(self):
        return self.partido

    def thumb_partido(self):
        from sorl.thumbnail import get_thumbnail
        if not self.logo:
            return ""
        from django.utils.safestring import mark_safe
        return mark_safe(f'<img src="{get_thumbnail(self.logo, "100", crop="center", quality=95).url}" />')
    thumb_partido.short_description = 'Logo'


class Candidato(models.Model):
    nombre = models.CharField(max_length=255)
    foto = sorl_thumbnail_ImageField(max_length=255, upload_to="imagenes/fotos-candidatos/")
    partido = models.ForeignKey(Partido, on_delete=models.PROTECT)
    slug = AutoSlugField(populate_from='nombre', unique=True, editable=False)

    def __str__(self):
        return self.nombre

    def thumb_partido(self):

        return self.partido.thumb_partido()

    thumb_partido.short_description = 'Logo'


class TipoEleccion(models.TextChoices):
    Pasos = "P", "Pasos"
    Generales = "G", "Generales"


class Eleccion(models.Model):
    anio = models.IntegerField(default=2023, verbose_name="Año")
    tipo_eleccion = models.CharField(max_length=1, choices=TipoEleccion.choices, default=TipoEleccion.Pasos)
    fecha_comicios = models.DateField()

    class Meta:
        verbose_name_plural = "Elecciones"

    def __str__(self):
        return f"{self.get_tipo_eleccion_display()} {self.anio}"


class Cargo(models.TextChoices):
    Presidente = "P", "Presidente"
    Gobernador = "G", "Gobernador"
    DipuNacional = "DN", "Diputado nacional"
    SenaNacional = "SN", "Senador nacional"
    DipuProvincial = "DP", "Diputado provincial"
    SenaProvincial = "SP", "Senador provincial"
    JefeGobierno = "J", "Jefe de gobierno"
    Intendente = "I", "Intendente"
    PresidenteComunal = "PC", "Presidente comunal"
    Concejal = "C", "Concejal"


class CargoElecto(models.Model):
    from smart_selects.db_fields import ChainedForeignKey

    candidato = models.ForeignKey(Candidato, on_delete=models.PROTECT)
    eleccion = models.ForeignKey(Eleccion, on_delete=models.PROTECT)
    cargo = models.CharField(max_length=2, choices=Cargo.choices)
    pais = models.ForeignKey(Country, on_delete=models.PROTECT, verbose_name="País")
    provincia = ChainedForeignKey(
        Region,
        chained_field="pais",
        chained_model_field="country",
        show_all=False,
        auto_choose=True,
        sort=True, null=True, blank=True)
    localidad = ChainedForeignKey(
        City,
        chained_field="provincia",
        chained_model_field="region",
        show_all=False,
        auto_choose=True,
        sort=True, null=True, blank=True)
    cant_votos = models.IntegerField(default=0)
    ult_actualizacion = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.candidato} --> {self.get_cargo_display()} ({self.eleccion})"
