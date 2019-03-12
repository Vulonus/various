#für Datei i/o:
import sys
import csv

# # Log-Datei der Firewall einlesen:
firewall = list(csv.reader(open("firewall.csv"), delimiter=';'))
for row in firewall:
    if row[3] == '445' and row[4] == 'Drop':
        print(row[0])
# # Test-Ausgabe der Liste:
# print(firewall)