import csv

with open("produkter_raw.csv", 'rb') as produkter:
    produkter_csv = csv.reader(produkter, delimiter=';')
    new_csv = []
    produkter_csv.next()
    for row in produkter_csv:
        alk = float(row[26])
        row.append(float(row[5]) / alk if alk > 0 else 9000.01)
        new_csv.append(row)

with open("produkter.csv", 'wb') as produkter:
    writer = csv.writer(produkter)
    writer.writerows(new_csv)
