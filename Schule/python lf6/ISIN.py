def isin_prüfen(isin):
    print('ISIN wird geprüft...')
    if isin[:2] != 'DE' or len(isin) != 12:
        return 'ISIN ungültig! Initialcode ungültig oder Nummernlänge inkorrekt!'
    #DE000BAY0017
    prüzi = str(isin_prüzi(isin[:11]))
    print(isin[11])
    print(prüzi)
    if prüzi == isin[11]:
        return 'ISIN gültig!'
    else:
        return 'ISIN ungültig!'

def isin_prüzi(isin):
    qrs = 0
    qrs_string = ''
    for zeichen in isin:
        if "A" <= zeichen <= "Z":
            qrs_string += str(10 + ord(zeichen) - ord("A"))
        else:
            qrs_string += zeichen
    index = 0
    for zahl in qrs_string:
        index += 1
        if index % 2 == 0:
            qrs += int(zahl) *2
        else:
            qrs += int(zahl)
    prüzi = (10 - (qrs % 10)) % 10
    return prüzi

def isin_check():
    while True:
        print('Prüzi bestimmen = 1\nISIN prüfen = 2\nEnde = 99')
        auswahl = input()
        if auswahl == '1':
            print('ISIN eingeben:')
            isin = input()
            prüzi = isin_prüzi(isin)
            print(prüzi)
        elif auswahl == '2':
            print('ISIN eingeben:')
            test = isin_prüfen(input())
            print(test)
        elif auswahl == '99':
            break
        else:
            print('Ungültige Auswahl!')

if __name__ == "__main__":
    isin_check()