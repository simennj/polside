import urllib
import csv
import subprocess

produkterlaster = urllib.URLopener()
produkterlaster.retrieve("http://www.vinmonopolet.no/api/produkter", "produkter_raw.csv")
produkterlaster.close()

subprocess.call("sed -i 's/,/./g' produkter_raw.csv")

with open("produkter_raw.csv", 'rb') as produkter:
    produkter_csv = csv.reader(produkter, delimiter=';')
    new_csv = []

    for row in produkter_csv:
        row.append(9000.01)
        new_csv.append(row)

with open("produkter.csv", 'wb') as produkter:
    writer = csv.writer(produkter)
    writer.writerows(new_csv)