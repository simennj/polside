# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


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

    def save(self, *args, **kwargs):
        self.enhetspris = self.pris_per_enhet()
        super(Produkter, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.varenavn

    def pris_per_enhet(self):
        if self.alkohol > 0:
            return self.literpris/self.alkohol
        return 9001

