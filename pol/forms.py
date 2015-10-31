# -*- coding: utf-8 -*-
from django import forms


class VarenavnForm(forms.Form):
    varenavn = forms.CharField(max_length=80, label='', required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Søk'}))


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
    varetype = forms.MultipleChoiceField(label='', choices=CHOICES, widget=forms.CheckboxSelectMultiple(),
                                         required=False)


class PrisForm(forms.Form):
    pris_0 = forms.DecimalField(required=False, label='',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Min'}))
    pris_1 = forms.DecimalField(required=False, label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Maks'}))


class VolumForm(forms.Form):
    volum_0 = forms.DecimalField(min_value=0, label='', required=False,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Min'}))
    volum_1 = forms.DecimalField(min_value=0, label='', required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Maks'}))


class AlkoholForm(forms.Form):
    alkohol_0 = forms.DecimalField(min_value=0, label='', required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Min'}))
    alkohol_1 = forms.DecimalField(min_value=0, label='', required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Maks'}))


class EnhetsprisForm(forms.Form):
    enhetspris_0 = forms.DecimalField(min_value=0, label='', required=False,
                                      widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Min'}))
    enhetspris_1 = forms.DecimalField(min_value=0, label='', required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Maks'}))


class Butikkategoriform(forms.Form):
    butikkategori = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Kategori 1-7'}))

class SorteringsForm(forms.Form):
    CHOICES = (
        ('enhetspris', 'enhetspris'),
        ('-enhetspris', '-enhetspris'),
        ('alkohol', 'alkohol'),
        ('-alkohol', '-alkohol'),
        ('volum', 'volum'),
        ('-volum', '-volum'),
        ('pris', 'pris'),
        ('-pris', '-pris'),
        ('varetype', 'varetype'),
        ('-varetype', '-varetype'),
        ('varenavn', 'varenavn'),
        ('-varenavn', '-varenavn'),
    )
    o = forms.MultipleChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect(),
        label='Sorter etter:',
    )
