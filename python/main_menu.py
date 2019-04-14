import os


if __name__ == "__main__":
    while True:
        print('#######  HAUPTMENÜ  ########')
        print('1 - Übung Kundennummer Generation und -prüfung')
        print('2 - Ping')
        print('3 - ISIN Prüzi, Prüfung')
        print('99 - Beenden')
        auswahl = input()
        if auswahl == '1':
            from kdnr_gen_check import kdnr_gen_check,Kundennummer_generieren,Kundennummer_prüfen
            kdnr_gen_check()
        elif auswahl == '2':
            from send_ping import send_ping
            send_ping()
        elif auswahl == '3':
            from ISIN import isin_prüfen,isin_check,isin_prüzi
            isin_check()
        elif auswahl == '99':
            print('Ende')
            break
        else:
            print('Ungültige Auswahl!')