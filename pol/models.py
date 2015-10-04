# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import django_filters


class Produkter(models.Model):
    datotid = models.DateTimeField(db_column='Datotid', blank=True, null=True)
    varenummer = models.IntegerField(db_column='Varenummer', primary_key=True)
    varenavn = models.CharField(db_column='Varenavn', max_length=80, blank=True, null=True)
    volum = models.DecimalField(db_column='Volum', max_digits=4, decimal_places=2, blank=True, null=True)
    pris = models.DecimalField(db_column='Pris', max_digits=7, decimal_places=2, blank=True, null=True)
    literpris = models.DecimalField(db_column='Literpris', max_digits=7, decimal_places=2, blank=True, null=True)
    varetype = models.CharField(db_column='Varetype', max_length=40, blank=True, null=True)
    produktutvalg = models.CharField(db_column='Produktutvalg', max_length=19, blank=True, null=True)
    butikkategori = models.CharField(db_column='Butikkategori', max_length=19, blank=True, null=True)
    fylde = models.IntegerField(db_column='Fylde', blank=True, null=True)
    friskhet = models.IntegerField(db_column='Friskhet', blank=True, null=True)
    garvestoffer = models.IntegerField(db_column='Garvestoffer', blank=True, null=True)
    bitterhet = models.IntegerField(db_column='Bitterhet', blank=True, null=True)
    sodme = models.IntegerField(db_column='Sodme', blank=True, null=True)
    farge = models.CharField(db_column='Farge', max_length=62, blank=True, null=True)
    lukt = models.CharField(db_column='Lukt', max_length=95, blank=True, null=True)
    smak = models.CharField(db_column='Smak', max_length=102, blank=True, null=True)
    passertil01 = models.CharField(db_column='Passertil01', max_length=20, blank=True, null=True)
    passertil02 = models.CharField(db_column='Passertil02', max_length=20, blank=True, null=True)
    passertil03 = models.CharField(db_column='Passertil03', max_length=20, blank=True, null=True)
    land = models.CharField(db_column='Land', max_length=15, blank=True, null=True)
    distrikt = models.CharField(db_column='Distrikt', max_length=20, blank=True, null=True)
    underdistrikt = models.CharField(db_column='Underdistrikt', max_length=22, blank=True, null=True)
    argang = models.CharField(db_column='Argang', max_length=4, blank=True, null=True)
    rastoff = models.CharField(db_column='Rastoff', max_length=124, blank=True, null=True)
    metode = models.CharField(db_column='Metode', max_length=205, blank=True, null=True)
    alkohol = models.DecimalField(db_column='Alkohol', max_digits=4, decimal_places=2, blank=True, null=True)
    sukker = models.CharField(db_column='Sukker', max_length=6, blank=True, null=True)
    syre = models.CharField(db_column='Syre', max_length=6, blank=True, null=True)
    lagringsgrad = models.CharField(db_column='Lagringsgrad', max_length=39, blank=True, null=True)
    produsent = models.CharField(db_column='Produsent', max_length=33, blank=True, null=True)
    grossist = models.CharField(db_column='Grossist', max_length=33, blank=True, null=True)
    distributor = models.CharField(db_column='Distributor', max_length=31, blank=True, null=True)
    emballasjetype = models.CharField(db_column='Emballasjetype', max_length=32, blank=True, null=True)
    korktype = models.CharField(db_column='Korktype', max_length=14, blank=True, null=True)
    vareurl = models.CharField(db_column='Vareurl', max_length=61, blank=True, null=True)
    enhetspris = models.DecimalField(db_column='Enhetspris', max_digits=7, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = 'produkter'
#        ordering = ('enhetspris',)

    def save(self, *args, **kwargs):
        self.enhetspris = self.pris_per_enhet()
        super(Produkter, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.varenavn

    def pris_per_enhet(self):
        if self.alkohol > 0:
            return self.literpris/self.alkohol
        return 9000.01


class ProduktFilter(django_filters.FilterSet):
    CHOICES =(
        ('Rødvin', 'Rødvin'),
        ('Hvitvin', 'Hvitvin'),
        ('Musserende Vin', 'Musserende Vin'),
        ('Øl', 'Øl'),
        ('Whisky', 'Whisky'),
        ('Druebrennevin', 'Druebrennevin'),
        ('Rosévin', 'Rosévin'),
        ('Akevitt', 'Akevitt'),
        ('Likør', 'Likør'),
        ('Vodka', 'Vodka'),
        ('Likør under 22 %', 'Likør under 22 %'),
        ('Portvin', 'Portvin'),
        ('Rom', 'Rom'),
        ('Fruktbrennevin', 'Fruktbrennevin'),
        ('Gin', 'Gin'),
        ('Øvrig Brennevin', 'Øvrig Brennevin'),
        ('Fruktvin', 'Fruktvin'),
        ('Øvrig Sterkvin', 'Øvrig Sterkvin'),
        ('Øvrig Brennevin under 22 %', 'Øvrig Brennevin under 22 %'),
        ('Bitter', 'Bitter'),
        ('Aromatisert Svakvin og annen blandet dri', 'Aromatisert Svakvin og annen blandet dri'),
        ('Sherry', 'Sherry'),
        ('Alkoholfritt', 'Alkoholfritt'),
        ('Vermut', 'Vermut'),
        ('Madeira', 'Madeira'),
        ('Bitter under 22 %', 'Bitter under 22 %'),
        ('Aromatisert Sterkvin', 'Aromatisert Sterkvin'),
        ('Musserende Fruktvin', 'Musserende Fruktvin'),
        ('Genever', 'Genever'),
        ('Øvrig Svakvin', 'Øvrig Svakvin'),
    )
    model = Produkter
    varetype = django_filters.MultipleChoiceFilter(choices=CHOICES)
    varenavn = django_filters.CharFilter(lookup_type='icontains')
    pris = django_filters.RangeFilter()
    volum = django_filters.RangeFilter()
    alkohol = django_filters.RangeFilter()
    enhetspris = django_filters.RangeFilter()

    class Meta:
        fields = (
            'varenavn',
            'varetype',
            'pris',
            'volum',
            'alkohol',
            'enhetspris',
        )
        order_by = (
            'varenavn',
            'varetype',
            'pris',
            'volum',
            'alkohol',
            'enhetspris',
        )


class Butikker(models.Model):
    datotid = models.CharField(db_column='Datotid', max_length=19, blank=True, null=True)
    butikknavn = models.CharField(db_column='Butikknavn', max_length=31, blank=True, null=True)
    gateadresse = models.CharField(db_column='Gateadresse', max_length=37, blank=True, null=True)
    gate_postnummer = models.IntegerField(db_column='Gate_postnummer', blank=True, null=True)
    gate_poststed = models.CharField(db_column='Gate_poststed', max_length=17, blank=True, null=True)
    postadresse = models.CharField(db_column='Postadresse', max_length=37, blank=True, null=True)
    post_postnummer = models.IntegerField(db_column='Post_postnummer', blank=True, null=True)
    post_poststed = models.CharField(db_column='Post_poststed', max_length=17, blank=True, null=True)
    telefonnummer = models.IntegerField(db_column='Telefonnummer', blank=True, null=True)
    kategori = models.CharField(db_column='Kategori', max_length=10, blank=True, null=True)
    gps_breddegrad = models.DecimalField(db_column='GPS_breddegrad', max_digits=12, decimal_places=10, blank=True, null=True)
    gps_lengdegrad = models.DecimalField(db_column='GPS_lengdegrad', max_digits=12, decimal_places=11, blank=True, null=True)
    ukenummer = models.IntegerField(db_column='Ukenummer', blank=True, null=True)
    apn_mandag = models.CharField(db_column='Apn_mandag', max_length=11, blank=True, null=True)
    apn_tirsdag = models.CharField(db_column='Apn_tirsdag', max_length=11, blank=True, null=True)
    apn_onsdag = models.CharField(db_column='Apn_onsdag', max_length=11, blank=True, null=True)
    apn_torsdag = models.CharField(db_column='Apn_torsdag', max_length=11, blank=True, null=True)
    apn_fredag = models.CharField(db_column='Apn_fredag', max_length=11, blank=True, null=True)
    apn_lordag = models.CharField(db_column='Apn_lordag', max_length=11, blank=True, null=True)
    ukenummer_neste = models.IntegerField(db_column='Ukenummer_neste', blank=True, null=True)
    apn_neste_mandag = models.CharField(db_column='Apn_neste_mandag', max_length=11, blank=True, null=True)
    apn_neste_tirsdag = models.CharField(db_column='Apn_neste_tirsdag', max_length=11, blank=True, null=True)
    apn_neste_onsdag = models.CharField(db_column='Apn_neste_onsdag', max_length=11, blank=True, null=True)
    apn_neste_torsdag = models.CharField(db_column='Apn_neste_torsdag', max_length=11, blank=True, null=True)
    apn_neste_fredag = models.CharField(db_column='Apn_neste_fredag', max_length=11, blank=True, null=True)
    apn_neste_lordag = models.CharField(db_column='Apn_neste_lordag', max_length=11, blank=True, null=True)
