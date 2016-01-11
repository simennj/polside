from models import Produkter, BolItems
from rest_framework import serializers


class ProduktSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Produkter
        fields = (
            'varenavn',
            'varetype',
            'pris',
            'volum',
            'alkohol',
            'enhetspris',
        )


class BolSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = BolItems