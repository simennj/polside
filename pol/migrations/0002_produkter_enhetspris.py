# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pol', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produkter',
            name='enhetspris',
            field=models.DecimalField(null=True, decimal_places=2, max_digits=7, db_column='Enhetspris', blank=True),
        ),
    ]
