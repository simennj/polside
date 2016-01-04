#!/usr/bin/env bash
curl -o bol-raw.xml http://www.systembolaget.se/api/assortment/products/xml
curl -o bolsort.xml http://www.systembolaget.se/api/assortment/stock/xml
sed -i 's/<skapad-tid>.*<\/info>//g' bol-raw.xml
sed -i 's/%//g' bol-raw.xml
sed -i 's/.*"2310"/<Butik/;s/<\/Butik>.*/<\/Butik>/' bolsort.xml
python2.7 bol.py
mysql -u simennj -p"aldri_mer_PHP" polguide < bol.sql
