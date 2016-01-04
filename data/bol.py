# coding=utf-8
import string
import urllib
import xml.etree.ElementTree as ET
import unicodedata
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
}

for i, oldItem in enumerate(root):
    if oldItem[0].text not in assortment:
        continue

    item = ET.SubElement(items, 'row')

    nr = ET.SubElement(item, 'field', {'name': 'nr'})
    name = ET.SubElement(item, 'field', {'name': 'name'})
    group = ET.SubElement(item, 'field', {'name': 'group'})
    producer = ET.SubElement(item, 'field', {'name': 'producer'})
    country = ET.SubElement(item, 'field', {'name': 'country'})
    price = ET.SubElement(item, 'field', {'name': 'price'})
    volume = ET.SubElement(item, 'field', {'name': 'volume'})
    alcohol = ET.SubElement(item, 'field', {'name': 'alcohol'})
    alcoholPrice = ET.SubElement(item, 'field', {'name': 'alcoholPrice'})
    url = ET.SubElement(item, 'field', {'name': 'url'})

    nr.text = oldItem.find('nr').text if oldItem.find('nr') is not None else ''
    name.text = oldItem.find('Namn').text if oldItem.find('Namn') is not None else ''
    group.text = oldItem.find('Varugrupp').text if oldItem.find('Varugrupp') is not None else ''
    producer.text = oldItem.find('Producent').text if oldItem.find('Producent') is not None else ''
    country.text = oldItem.find('Ursprunglandnamn').text if oldItem.find('Ursprunglandnamn') is not None else ''
    price.text = oldItem.find('Prisinklmoms').text if oldItem.find('Prisinklmoms') is not None else ''
    volume.text = oldItem.find('Volymiml').text if oldItem.find('Volymiml') is not None else ''
    alcohol.text = oldItem.find('Alkoholhalt').text if oldItem.find('Alkoholhalt') is not None else ''

    volume.text = '{0:.1f}'.format(float(volume.text) / 10)
    groupText = group.text
    if groupText[:1] == 'sm':
        if groupText[-1] == 't':
            urlGroup = 'sprit'
        else:
            urlGroup = 'aperitif-dessert'
    else:
        urlGroup = urlGroupDict[unicode(groupText[:2])]
    url.text = urlGroup + '/' + slugify(unicode(name.text.replace(' ', '-').lower())) + '-' + nr.text

    alcoholValue = float(alcohol.text)
    alcoholPrice.text = '{0:.2f}'.format(
        float(oldItem.find('PrisPerLiter').text) / alcoholValue if alcoholValue > 0 else 9000.01)

tree = ET.ElementTree(items)
tree.write('bol.xml', 'utf-8')
# assortment.remove(item[0].text)
# if len(oldItem) == 24: del oldItem[23]
# del oldItem[22], oldItem[21], oldItem[16:18], oldItem[11:13], oldItem[7:9], oldItem[4], oldItem[2], oldItem[1]
# items.append(oldItem)
