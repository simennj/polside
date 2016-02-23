#!/bin/bash
python2.7 retrievedata.py
sed -i 's/,/./g' produkter_raw.csv
python2.7 formatdata.py
mysql -u simennj -p"PHP_er_ubrukelig" polguide < deletedata.sql
mysql -u simennj -p"PHP_er_ubrukelig" polguide < uploaddata.sql