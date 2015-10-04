# -*- coding: utf-8 -*-
from django import forms

from .models import ProduktFilter, Produkter


class VarenavnForm(forms.Form):
    varenavn = forms.CharField(max_length=80,required=False)


class VaretypeForm(forms.Form):
    CHOICES = (
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
    varetype = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple(), required=False)


class PrisForm(forms.Form):
    pris_0 = forms.DecimalField(required=False, label='minpris')
    pris_1 = forms.DecimalField(required=False, label='makspris')


class VolumForm(forms.Form):
    volum_0 = forms.DecimalField(min_value=0, required=False)
    volum_1 = forms.DecimalField(min_value=0, required=False)


class AlkoholForm(forms.Form):
    alkohol_0 = forms.DecimalField(min_value=0, required=False)
    alkohol_1 = forms.DecimalField(min_value=0, required=False)


class EnhetsprisForm(forms.Form):
    enhetspris_0 = forms.DecimalField(min_value=0, required=False)
    enhetspris_1 = forms.DecimalField(min_value=0, required=False)


class SorteringsForm(forms.Form):
    CHOICES = (
        ('enhetspris', 'enhetspris'),
        ('alkohol', 'alkohol'),
        ('volum', 'volum'),
        ('pris', 'pris'),
        ('varetype', 'varetype'),
        ('varenavn', 'varenavn'),
    )
    o = forms.MultipleChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect(),
    )
