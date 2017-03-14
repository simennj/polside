# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import django_filters
from django.db import models
from django.db.models import Lookup


class Butikkategorilookup(Lookup):
    lookup_name = 'bkat'

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        print len(rhs_params[0])
        rhs_params[0] = 'Butikkategori ' + rhs_params[0][-1]
        params = lhs_params + rhs_params
        return '%s <= %s' % (lhs, rhs), params
        # TODO: Do this properly if i ever learn the API


class BolItems(models.Model):
    nr = models.IntegerField(primary_key=True)
    navn = models.CharField(max_length=50)
    beskrivelse = models.CharField(max_length=36, blank=True, null=True)
    kategori = models.CharField(max_length=22)
    produsent = models.CharField(max_length=71, blank=True, null=True)
    land = models.CharField(max_length=23, blank=True, null=True)
    pris = models.DecimalField(max_digits=7, decimal_places=2)
    volum = models.DecimalField(max_digits=5, decimal_places=1)
    alkohol = models.DecimalField(max_digits=4, decimal_places=2)
    alkoholpris = models.DecimalField(max_digits=6, decimal_places=2)
    url = models.CharField(max_length=100)


class BolFilter(django_filters.FilterSet):
    groups = (
        ('ol', 'ol'),
        ('sprit', 'sprit'),
        ('aperitif-dessert', 'aperitif-dessert'),
        ('mousserande-viner', 'mousserande-viner'),
        ('roda-viner', 'roda-viner'),
        ('cider-och-blanddrycker', 'cider-och-blanddrycker'),
        ('vita-viner', 'vita-viner'),
        ('alkoholfritt', 'alkoholfritt'),
    )

    navn = django_filters.MultipleChoiceFilter(choices=groups)
    kategori = django_filters.CharFilter(lookup_type='icontains')
    produsent = django_filters.CharFilter(lookup_type='icontains')
    land = django_filters.CharFilter(lookup_type='icontains')
    pris = django_filters.RangeFilter()
    volum = django_filters.RangeFilter()
    alkohol = django_filters.RangeFilter()
    alkoholpris = django_filters.RangeFilter()

    class Meta:
        model = BolItems
        order_by = (
            'alkoholpris',
            '-alkoholpris',
            'navn',
            '-navn',
            'kategori',
            '-kategori',
            'pris',
            '-pris',
            'volum',
            '-volum',
            'alkohol',
            '-alkohol',
        )


# class PolItems(models.Model):
#    nr = models.IntegerField(primary_key=True)
#    name = models.CharField(max_length=80)
#    group = models.CharField(max_length=40, blank=True, null=True)
#    producer = models.CharField(max_length=33, blank=True, null=True)
#    country = models.CharField(max_length=15, blank=True, null=True)
#    price = models.DecimalField(max_digits=7, decimal_places=2)
#    volume = models.DecimalField(max_digits=4, decimal_places=2)
#    alcohol = models.DecimalField(max_digits=4, decimal_places=2)
#    alcoholPrice = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)

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

    butikkategori.register_lookup(Butikkategorilookup)  # TODO: kan denne fjernes?

    class Meta:
        db_table = 'produkter'

    def save(self, *args, **kwargs):
        self.enhetspris = self.pris_per_enhet()
        super(Produkter, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.varenavn

    def pris_per_enhet(self):
        if self.alkohol > 0:
            return self.literpris / self.alkohol
        return 9000.01


class ProduktFilter(django_filters.FilterSet):
    CHOICES = (
        ('Akevitt', 'Akevitt'),
        ('Portvin', 'Portvin'),
        ('Vodka', 'Vodka'),
        ('Druebrennevin', 'Druebrennevin'),
        ('Whisky', 'Whisky'),
        ('Likør', 'Likør'),
        ('Genever', 'Genever'),
        ('Gin', 'Gin'),
        ('Bitter', 'Bitter'),
        ('Fruktbrennevin', 'Fruktbrennevin'),
        ('Vermut', 'Vermut'),
        ('Aromatisert vin', 'Aromatisert vin'),
        ('Brennevin. annet', 'Brennevin. annet'),
        ('Sherry', 'Sherry'),
        ('Rødvin', 'Rødvin'),
        ('Hvitvin', 'Hvitvin'),
        ('Perlende vin. rosé', 'Perlende vin. rosé'),
        ('Champagne. brut', 'Champagne. brut'),
        ('Champagne. sec', 'Champagne. sec'),
        ('Musserende vin. rosé', 'Musserende vin. rosé'),
        ('Champagne. rosé', 'Champagne. rosé'),
        ('Musserende vin', 'Musserende vin'),
        ('Alkoholfri most', 'Alkoholfri most'),
        ('Alkoholfritt. øvrig', 'Alkoholfritt. øvrig'),
        ('Rosévin', 'Rosévin'),
        ('Porter & stout', 'Porter & stout'),
        ('Alkoholfritt øl', 'Alkoholfritt øl'),
        ('Champagne extra brut', 'Champagne extra brut'),
        ('India pale ale', 'India pale ale'),
        ('Saison farmhouse ale', 'Saison farmhouse ale'),
        ('Lys ale', 'Lys ale'),
        ('Rom', 'Rom'),
        ('Klosterstil', 'Klosterstil'),
        ('Spesial', 'Spesial'),
        ('Mørk lager', 'Mørk lager'),
        ('Barley wine', 'Barley wine'),
        ('Hveteøl', 'Hveteøl'),
        ('Pale ale', 'Pale ale'),
        ('Perlende vin. rød', 'Perlende vin. rød'),
        ('Sterkvin. annen', 'Sterkvin. annen'),
        ('Fruktvin', 'Fruktvin'),
        ('Sider', 'Sider'),
        ('Perlende vin. hvit', 'Perlende vin. hvit'),
        ('Brown ale', 'Brown ale'),
        ('Alkoholfri vin', 'Alkoholfri vin'),
        ('Alkoholfri musserende drikk', 'Alkoholfri musserende drikk'),
        ('Lys lager', 'Lys lager'),
        ('Alkoholfri leskedrikk', 'Alkoholfri leskedrikk'),
        ('Red/amber', 'Red/amber'),
        ('Sake', 'Sake'),
        ('Surøl', 'Surøl'),
        ('Madeira', 'Madeira'),
        ('Mjød', 'Mjød'),
        ('Brennevin. nøytralt < 37.5 %', 'Brennevin. nøytralt < 37.5 %'),
        ('Champagne. annen', 'Champagne. annen'),
    )
    varetype = django_filters.MultipleChoiceFilter(choices=CHOICES)
    varenavn = django_filters.CharFilter(lookup_type='icontains')
    pris = django_filters.RangeFilter()
    volum = django_filters.RangeFilter()
    alkohol = django_filters.RangeFilter()
    enhetspris = django_filters.RangeFilter()
    butikkategori = django_filters.CharFilter(lookup_type='bkat')
    land = django_filters.CharFilter(lookup_type='icontains')
    produsent = django_filters.CharFilter(lookup_type='icontains')

    class Meta:
        model = Produkter
        fields = (
            'varenavn',
            'varetype',
            'pris',
            'volum',
            'alkohol',
            'enhetspris',
            'butikkategori',
            'land',
            'produsent'
        )
        order_by = (
            'enhetspris',
            '-enhetspris',
            'varenavn',
            '-varenavn',
            'varetype',
            '-varetype',
            'pris',
            '-pris',
            'volum',
            '-volum',
            'alkohol',
            '-alkohol',
        )

# class Butikker(models.Model):
#    datotid = models.CharField(db_column='Datotid', max_length=19, blank=True, null=True)
#    butikknavn = models.CharField(db_column='Butikknavn', max_length=31, blank=True, null=True)
#    gateadresse = models.CharField(db_column='Gateadresse', max_length=37, blank=True, null=True)
#    gate_postnummer = models.IntegerField(db_column='Gate_postnummer', blank=True, null=True)
#    gate_poststed = models.CharField(db_column='Gate_poststed', max_length=17, blank=True, null=True)
#    postadresse = models.CharField(db_column='Postadresse', max_length=37, blank=True, null=True)
#    post_postnummer = models.IntegerField(db_column='Post_postnummer', blank=True, null=True)
#    post_poststed = models.CharField(db_column='Post_poststed', max_length=17, blank=True, null=True)
#    telefonnummer = models.IntegerField(db_column='Telefonnummer', blank=True, null=True)
#    kategori = models.CharField(db_column='Kategori', max_length=10, blank=True, null=True)
#    gps_breddegrad = models.DecimalField(db_column='GPS_breddegrad', max_digits=12, decimal_places=10, blank=True,
#                                         null=True)
#    gps_lengdegrad = models.DecimalField(db_column='GPS_lengdegrad', max_digits=12, decimal_places=11, blank=True,
#                                         null=True)
#    ukenummer = models.IntegerField(db_column='Ukenummer', blank=True, null=True)
#    apn_mandag = models.CharField(db_column='Apn_mandag', max_length=11, blank=True, null=True)
#    apn_tirsdag = models.CharField(db_column='Apn_tirsdag', max_length=11, blank=True, null=True)
#    apn_onsdag = models.CharField(db_column='Apn_onsdag', max_length=11, blank=True, null=True)
#    apn_torsdag = models.CharField(db_column='Apn_torsdag', max_length=11, blank=True, null=True)
#    apn_fredag = models.CharField(db_column='Apn_fredag', max_length=11, blank=True, null=True)
#    apn_lordag = models.CharField(db_column='Apn_lordag', max_length=11, blank=True, null=True)
#    ukenummer_neste = models.IntegerField(db_column='Ukenummer_neste', blank=True, null=True)
#    apn_neste_mandag = models.CharField(db_column='Apn_neste_mandag', max_length=11, blank=True, null=True)
#    apn_neste_tirsdag = models.CharField(db_column='Apn_neste_tirsdag', max_length=11, blank=True, null=True)
#    apn_neste_onsdag = models.CharField(db_column='Apn_neste_onsdag', max_length=11, blank=True, null=True)
#    apn_neste_torsdag = models.CharField(db_column='Apn_neste_torsdag', max_length=11, blank=True, null=True)
#    apn_neste_fredag = models.CharField(db_column='Apn_neste_fredag', max_length=11, blank=True, null=True)
#    apn_neste_lordag = models.CharField(db_column='Apn_neste_lordag', max_length=11, blank=True, null=True)
