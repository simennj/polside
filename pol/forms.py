# -*- coding: utf-8 -*-
from django import forms


class VarenavnForm(forms.Form):
    varenavn = forms.CharField(max_length=80, label='', required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Søk'}))


class VaretypeForm(forms.Form):
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
    varetype = forms.MultipleChoiceField(label='', choices=CHOICES,
                                         widget=forms.SelectMultiple(
                                                 attrs={'class': 'selectpicker', 'title': 'Velg varetyper'}),
                                         required=False)


class PrisForm(forms.Form):
    pris_0 = forms.DecimalField(required=False, label='',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Min'}))
    pris_1 = forms.DecimalField(required=False, label='',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Maks'}))


class VolumForm(forms.Form):
    volum_0 = forms.DecimalField(min_value=0, label='', required=False,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Min'}))
    volum_1 = forms.DecimalField(min_value=0, label='', required=False,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Maks'}))


class AlkoholForm(forms.Form):
    alkohol_0 = forms.DecimalField(min_value=0, label='', required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Min'}))
    alkohol_1 = forms.DecimalField(min_value=0, label='', required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Maks'}))


class EnhetsprisForm(forms.Form):
    enhetspris_0 = forms.DecimalField(min_value=0, label='', required=False,
                                      widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Min'}))
    enhetspris_1 = forms.DecimalField(min_value=0, label='', required=False,
                                      widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Maks'}))


class LandForm(forms.Form):
    land = forms.CharField(label='', required=False, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Søk'}))


class ProdusentForm(forms.Form):
    produsent = forms.CharField(label='', required=False, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Søk'}))


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
    o = forms.ChoiceField(
            choices=CHOICES,
            label='',
            required=False
    )


class BolForm(forms.Form):
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

    sortChoices = (
        'alcoholPrice',
        '-alcoholPrice',
        'name',
        '-name',
        'group',
        '-group',
        'price',
        '-price',
        'volume',
        '-volume',
        'alcohol',
        '-alcohol',
    )
    navn = forms.CharField(max_length=80, label='', required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Søk'}))

    kategori = forms.MultipleChoiceField(label='', choices=groups,
                                         widget=forms.SelectMultiple(
                                                 attrs={'class': 'selectpicker', 'title': 'Velg kategori'}),
                                         required=False)

    pris_0 = forms.DecimalField(required=False, label='',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Min'}))
    pris_1 = forms.DecimalField(required=False, label='',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Maks'}))

    volum_0= forms.DecimalField(min_value=0, label='', required=False,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Min'}))
    volum_1 = forms.DecimalField(min_value=0, label='', required=False,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Maks'}))

    alkohol_0= forms.DecimalField(min_value=0, label='', required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Min'}))
    alkohol_1 = forms.DecimalField(min_value=0, label='', required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Maks'}))

    alkoholpris_0 = forms.DecimalField(min_value=0, label='', required=False,
                                      widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Min'}))
    alkoholpris_1 = forms.DecimalField(min_value=0, label='', required=False,
                                      widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Maks'}))

    land = forms.CharField(label='', required=False, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Søk'}))

    produsent = forms.CharField(label='', required=False, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Søk'}))

    o = forms.ChoiceField(
            choices=sortChoices,
            label='',
            required=False
    )
