# coding=utf-8
import xml.etree.ElementTree as ET

import json
from django.utils.text import slugify

rawTree = ET.parse('bol-raw.xml')
root = rawTree.getroot()

assortmentTree = ET.parse('bolsort.xml')
assortmentRoot = assortmentTree.getroot()
assortment = set([oldItem.text for oldItem in assortmentRoot])
items = ET.Element('pol_bolitems')
jsonItems = []
jsonAllItems = []

urlGroupDict = {
    u'Öl': 'ol',
    u'Kr': 'sprit',
    u'Po': 'aperitif-dessert',
    u'Mo': 'mousserande-viner',
    u'Rö': 'roda-viner',
    u'Pu': 'sprit',
    u'Li': 'sprit',
    u'Ma': 'aperitif-dessert',
    u'Ro': 'sprit',
    u'Fr': 'aperitif-dessert',
    u'Te': 'sprit',
    u'Bl': 'cider-och-blanddrycker',
    u'Bi': 'sprit',
    u'Wh': 'sprit',
    u'Br': 'sprit',
    u'Dr': 'sprit',
    u'Ok': 'sprit',
    u'Sh': 'aperitif-dessert',
    u'Sa': 'aperitif-dessert',
    u'Gr': 'sprit',
    u'Ci': 'cider-och-blanddrycker',
    u'Co': 'sprit',
    u'Ve': 'aperitif-dessert',
    u'Vi': 'vita-viner',
    u'Ca': 'sprit',
    u'Al': 'alkoholfritt',
    u'An': 'sprit',
    u'Ap': 'aperitif-dessert',
    u'Ar': 'sprit',
    u'Öv': 'aperitif-dessert',
    u'Gl': 'aperitif-dessert',
    u'Gi': 'sprit',
    u'Sp': 'sprit',
    u'Ge': 'sprit',
    u'Mj': 'aperitif-dessert',
}

for i, oldItem in enumerate(root):
    jsonItem = dict()

    jsonItem["nr"] = int(oldItem.find('nr').text)
    jsonItem['navn'] = oldItem.find('Namn').text
    jsonItem['beskrivelse'] = oldItem.find('Varugrupp').text if oldItem.find('Varugrupp') is not None else ''
    jsonItem['produsent'] = oldItem.find('Producent').text if oldItem.find('Producent') is not None else ''
    jsonItem['land'] = oldItem.find('Ursprunglandnamn').text if oldItem.find('Ursprunglandnamn') is not None else ''
    jsonItem['pris'] = float(oldItem.find('Prisinklmoms').text)
    jsonItem['volum'] = float(oldItem.find('Volymiml').text)
    jsonItem['alkohol'] = float(oldItem.find('Alkoholhalt').text)

    jsonItem['volum'] /= 10
    beskrivelsestekst = jsonItem['beskrivelse']
    if beskrivelsestekst[:2] == 'Sm':
        if beskrivelsestekst[-1] == 't':
            kategoritekst = 'sprit'
        else:
            kategoritekst = 'aperitif-dessert'
    elif beskrivelsestekst[:3] == 'Ros':
        kategoritekst = 'roseviner'
    else:
        kategoritekst = urlGroupDict[unicode(beskrivelsestekst[:2])]
    jsonItem['url'] = kategoritekst + '/' + slugify(unicode(jsonItem['navn'].replace(' ', '-').lower())) + '-' + \
                      unicode(jsonItem['nr'])

    jsonItem['kategori'] = kategoritekst

    alcoholValue = float(jsonItem['alkohol'])
    jsonItem['alkoholpris'] = (float(oldItem.find('PrisPerLiter').text) / alcoholValue if alcoholValue > 0 else 9000.01)
    if oldItem[0].text in assortment:
        jsonItems.append(jsonItem)
    jsonAllItems.append(jsonItem)

with open('bol.json', 'w') as jsonFile:
    jsonFile.write(json.dumps(jsonItems))
with open('bolall.json', 'w') as jsonAllFile:
    jsonAllFile.write(json.dumps(jsonAllItems))
