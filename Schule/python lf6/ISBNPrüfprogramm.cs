using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ISBNPrüfung
{
    public class ISBN
    {
        static void Main(string[] args)
        {
        }
        public int Prüziberechnung(string ISBNNummer)
        {
            //Hilfsvariablen initialisieren
            int prüzi = 0;
            int zwischenErgebnis = 0;
            string multiplikatorString = "131313131313";        //Multiplikator-Zahlen

            //Schleife zum Multiplizieren und Zusammenzählen der einzelnen Ziffern der ISBN
            for (int stelle = 0; stelle < 11; stelle++)
            {
                int zahl1 = Convert.ToInt32(ISBNNummer[stelle]) - Convert.ToInt32('0');
                int zahl2 = Convert.ToInt32(multiplikatorString[stelle]) - Convert.ToInt32('0');
                zwischenErgebnis += zahl1 * zahl2;
            }
            //Ergebnis durch 10 teilen und Rest prüfen. Danach Prüfziffer zurückgeben
            zwischenErgebnis = zwischenErgebnis % 10;
            if (zwischenErgebnis > 0)
                prüzi = 10 - zwischenErgebnis;

            return prüzi;
        }
    }
}