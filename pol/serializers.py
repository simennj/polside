from models import Produkter
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