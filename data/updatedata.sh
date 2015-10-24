#!/bin/bash
python2.7 retrievedata.py
sed -i 's/,/./g' produkter_raw.csv
python2.7 formatdata.py