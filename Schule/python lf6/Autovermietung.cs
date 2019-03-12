using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Autovermietung
{
    class Program
    {
        static void Main(string[] args)
        {
#
            //Deklarieren 
            int Arbeitstage;
            int Wochenende;
            int km;
            int freikmat;
            int freikmwe;
            int mehrkm;
            double Mieteat;
            double Mietewe;
            double Kostenmehrkm;
            double Gesamtkosten;
        
            //Eingabe der Werte 
            Console.Write("Bitte die gefahrenen Arbeitstage angeben: ");
            Arbeitstage = Convert.ToInt32(Console.ReadLine());

            Console.Write("Bitte die Anzahl der Wochenenden eingeben: ");
            Wochenende = Convert.ToInt32(Console.ReadLine());

            Console.Write("Bitte die gefahrenen Kilometer angeben: ");
            km = Convert.ToInt32(Console.ReadLine());

            //Speichern der Werte 
            freikmat = 100;
            freikmwe = 200;

            Mieteat = 75;
            Mietewe = 100;

            Kostenmehrkm = 0.35;

            //Rechnen der Zwischenwerte 
            if (Arbeitstage > 0 && km > 100)
            {
                mehrkm = km - Arbeitstage 
            }
          
        }
    }
}
