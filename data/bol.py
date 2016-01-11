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
    u'Sm': 'sprit',
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
    if oldItem[0].text not in assortment:
        continue

    item = ET.SubElement(items, 'row')

    nr = ET.SubElement(item, 'field', {'name': 'nr'})
    navn = ET.SubElement(item, 'field', {'name': 'navn'})
    beskrivelse = ET.SubElement(item, 'field', {'name': 'beskrivelse'})
    kategori = ET.SubElement(item, 'field', {'name': 'kategori'})
    produsent = ET.SubElement(item, 'field', {'name': 'produsent'})
    land = ET.SubElement(item, 'field', {'name': 'land'})
    pris = ET.SubElement(item, 'field', {'name': 'pris'})
    volum = ET.SubElement(item, 'field', {'name': 'volum'})
    alkohol = ET.SubElement(item, 'field', {'name': 'alkohol'})
    alkoholpris = ET.SubElement(item, 'field', {'name': 'alkoholpris'})
    url = ET.SubElement(item, 'field', {'name': 'url'})

    nr.text = oldItem.find('nr').text if oldItem.find('nr') is not None else ''
    navn.text = oldItem.find('Namn').text if oldItem.find('Namn') is not None else ''
    beskrivelse.text = oldItem.find('Varugrupp').text if oldItem.find('Varugrupp') is not None else ''
    produsent.text = oldItem.find('Producent').text if oldItem.find('Producent') is not None else ''
    land.text = oldItem.find('Ursprunglandnamn').text if oldItem.find('Ursprunglandnamn') is not None else ''
    pris.text = oldItem.find('Prisinklmoms').text if oldItem.find('Prisinklmoms') is not None else ''
    volum.text = oldItem.find('Volymiml').text if oldItem.find('Volymiml') is not None else ''
    alkohol.text = oldItem.find('Alkoholhalt').text if oldItem.find('Alkoholhalt') is not None else ''

    volum.text = '{0:.1f}'.format(float(volum.text) / 10)
    beskrivelsestekst = beskrivelse.text
    if beskrivelsestekst[:1] == 'sm':
        if beskrivelsestekst[-1] == 't':
            kategoritekst = 'sprit'
        else:
            kategoritekst = 'aperitif-dessert'
    elif beskrivelsestekst[:2] == 'ros':
        kategoritekst = 'roseviner'
    else:
        kategoritekst = urlGroupDict[unicode(beskrivelsestekst[:2])]
    url.text = kategoritekst + '/' + slugify(unicode(navn.text.replace(' ', '-').lower())) + '-' + nr.text

    kategori.text = kategoritekst

    alcoholValue = float(alkohol.text)
    alkoholpris.text = '{0:.2f}'.format(
            float(oldItem.find('PrisPerLiter').text) / alcoholValue if alcoholValue > 0 else 9000.01)

tree = ET.ElementTree(items)
tree.write('bol.xml', 'utf-8')
# assortment.remove(item[0].text)
# if len(oldItem) == 24: del oldItem[23]
# del oldItem[22], oldItem[21], oldItem[16:18], oldItem[11:13], oldItem[7:9], oldItem[4], oldItem[2], oldItem[1]
# items.append(oldItem)
