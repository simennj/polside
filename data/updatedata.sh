#!/bin/bash
python2.7 retrievedata.py
sed -i 's/,/./g' produkter_raw.csv
python2.7 formatdata.py
mysql -u simennj -p"aldri_mer_PHP" polguide < deletedata.sql
mysql -u simennj -p"aldri_mer_PHP" polguide < uploaddata.sql