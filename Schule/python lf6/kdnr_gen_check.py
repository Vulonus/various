
def Kundennummer_speichern(kundennummer):
    import os
    if os.path.isfile('./kundennummern.txt') and kundennummer in open('kundennummern.txt','rt').readlines():
        print('error: Kundennummer bereits vorhanden!')
    else:
        with open('kundennummern.txt','at') as kundennummern:
            kundennummern.write(kundennummer)
        print('Kundennummer gespeichert!')

def Kundennummer_prüfen(kundenummer):
    print('Kundennummer wird geprüft...')
    qrs = 0
    if kundenummer[:2] != 'RB' or len(kundenummer) != 12:
        return 'Kundenummer ungültig! Initialcode ungültig oder Nummernlänge inkorrekt!'
    for i in kundenummer[2:10]:
        qrs += int(i)
    prüzi = qrs + int(kundenummer[10:12])
    if prüzi == 98:
        return 'Kundennummer gültig!'
    else:
        return 'Kundennummer ungültig!'


def Kundennummer_generieren():
    import random
    print('Kundennummer generieren')
    _kundNr = 'RB'
    random.seed()
    quersumme = 0
    for i in range(0, 8):
        r = random.randint(1, 9)
        _kundNr += str(r)
        quersumme += r
    endstelle = 98 - quersumme
    _kundNr += str(endstelle)
    return _kundNr


def kdnr_gen_check():
    while True:
        print('Kundennummer generieren = 1\nKundennummer prüfen=2\nHauptmenü=99')
        auswahl = input()
        if auswahl == '1':
            kundNr = Kundennummer_generieren()
            print(kundNr)
            print('Kundennummer speichern? (Y/N)')
            speichern = input()
            if speichern in ['Y','y']:
                Kundennummer_speichern(kundNr)
            else:
                print('Kundennummer wurde nicht gespeichert.')
        elif auswahl == '2':
            print('Kundennummer eingeben:')
            test = Kundennummer_prüfen(input())
            print(test)
        elif auswahl == '99':
            break
        else:
            print('Ungültige Auswahl!')
