# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produkter',
            fields=[
                ('datotid', models.DateTimeField(null=True, db_column='Datotid', blank=True)),
                ('varenummer', models.IntegerField(serialize=False, primary_key=True, db_column='Varenummer')),
                ('varenavn', models.CharField(max_length=80, null=True, db_column='Varenavn', blank=True)),
                ('volum', models.DecimalField(null=True, decimal_places=2, max_digits=4, db_column='Volum', blank=True)),
                ('pris', models.DecimalField(null=True, decimal_places=2, max_digits=7, db_column='Pris', blank=True)),
                ('literpris', models.DecimalField(null=True, decimal_places=2, max_digits=7, db_column='Literpris', blank=True)),
                ('varetype', models.CharField(max_length=40, null=True, db_column='Varetype', blank=True)),
                ('produktutvalg', models.CharField(max_length=19, null=True, db_column='Produktutvalg', blank=True)),
                ('butikkategori', models.CharField(max_length=19, null=True, db_column='Butikkategori', blank=True)),
                ('fylde', models.IntegerField(null=True, db_column='Fylde', blank=True)),
                ('friskhet', models.IntegerField(null=True, db_column='Friskhet', blank=True)),
                ('garvestoffer', models.IntegerField(null=True, db_column='Garvestoffer', blank=True)),
                ('bitterhet', models.IntegerField(null=True, db_column='Bitterhet', blank=True)),
                ('sodme', models.IntegerField(null=True, db_column='Sodme', blank=True)),
                ('farge', models.CharField(max_length=62, null=True, db_column='Farge', blank=True)),
                ('lukt', models.CharField(max_length=95, null=True, db_column='Lukt', blank=True)),
                ('smak', models.CharField(max_length=102, null=True, db_column='Smak', blank=True)),
                ('passertil01', models.CharField(max_length=20, null=True, db_column='Passertil01', blank=True)),
                ('passertil02', models.CharField(max_length=20, null=True, db_column='Passertil02', blank=True)),
                ('passertil03', models.CharField(max_length=20, null=True, db_column='Passertil03', blank=True)),
                ('land', models.CharField(max_length=15, null=True, db_column='Land', blank=True)),
                ('distrikt', models.CharField(max_length=20, null=True, db_column='Distrikt', blank=True)),
                ('underdistrikt', models.CharField(max_length=22, null=True, db_column='Underdistrikt', blank=True)),
                ('argang', models.CharField(max_length=4, null=True, db_column='Argang', blank=True)),
                ('rastoff', models.CharField(max_length=124, null=True, db_column='Rastoff', blank=True)),
                ('metode', models.CharField(max_length=205, null=True, db_column='Metode', blank=True)),
                ('alkohol', models.DecimalField(null=True, decimal_places=2, max_digits=4, db_column='Alkohol', blank=True)),
                ('sukker', models.CharField(max_length=6, null=True, db_column='Sukker', blank=True)),
                ('syre', models.CharField(max_length=6, null=True, db_column='Syre', blank=True)),
                ('lagringsgrad', models.CharField(max_length=39, null=True, db_column='Lagringsgrad', blank=True)),
                ('produsent', models.CharField(max_length=33, null=True, db_column='Produsent', blank=True)),
                ('grossist', models.CharField(max_length=33, null=True, db_column='Grossist', blank=True)),
                ('distributor', models.CharField(max_length=31, null=True, db_column='Distributor', blank=True)),
                ('emballasjetype', models.CharField(max_length=32, null=True, db_column='Emballasjetype', blank=True)),
                ('korktype', models.CharField(max_length=14, null=True, db_column='Korktype', blank=True)),
                ('vareurl', models.CharField(max_length=61, null=True, db_column='Vareurl', blank=True)),
            ],
            options={
                'db_table': 'produkter',
            },
        ),
    ]
